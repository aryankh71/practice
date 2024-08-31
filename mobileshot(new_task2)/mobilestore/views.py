from django.http import HttpResponse
from .models import *
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# from .forms import ModelForm, ExtendedCommentForm, CustomUserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as pre_login, logout as pre_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from .models import ExtendedComment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from datetime import datetime
# from django.contrib.auth import login, authenticate
from django.views import View
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .utils import filter_bad_words, BAD_WORDS
from django.db import transaction
from django.views.decorators.http import require_POST
from .serializers import MobileSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import MobileSerializer
from rest_framework.response import Response

class MobileListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        mobile = Mobile.objects.all()
        serializer = MobileSerializer(mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(selfself, request, *args, **kwargs):
        data = request.data
        mobile = data.get("mobile")



@csrf_exempt
def Mobile_Post(request):
    if request.user.is_authenticated:
        try:
            mobiles = Mobile.objects.all()
            return render(request, 'brandpage.html', {'mobiles': mobiles})
        except Mobile.DoesNotExist:
            return render(request, '404.html', status=404)

    return render(request, 'forbidden.html', context={})


@login_required
def Mobile_Details(request, id):
    mobile = get_object_or_404(Mobile, id=id)
    similar_mobiles = Mobile.objects.filter(brand=mobile.brand).exclude(id=id)[:5]
    comments = mobile.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            cleaned_body = comment_form.cleaned_data['body']
            filtered_body = filter_bad_words(cleaned_body, BAD_WORDS)
            new_comment.body = filtered_body
            # filtered_text = filter_bad_words(new_comment.body, BAD_WORDS)
            # new_comment.body = filtered_text
            new_comment.mobile = mobile
            new_comment.user = request.user  # اطمینان حاصل کنید که کاربر را تنظیم می‌کنید
            new_comment.save()
            return redirect('mobiledetails', id=mobile.id)
    else:
        comment_form = CommentForm()

    context = {
        'mobile': mobile,
        'similar_mobiles': similar_mobiles,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'mobiledetails.html', context)


# @login_required
# def Mobile_Details(request, id):
#     mobile = get_object_or_404(Mobile, id=id)
#     similar_mobiles = Mobile.objects.filter(brand=mobile.brand).exclude(id=id)[:5]
#     comments = mobile.comments.filter(active=True)
#     new_comment = None
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         filtered_text = filter_bad_words(text, BAD_WORDS)
#         comment = Comment(text=filtered_text)
#         comment.save()
#         return redirect('comments')
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.mobile = mobile
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'mobile': mobile,
#         'similar_mobiles': similar_mobiles,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': comment_form,  # Add comment_form to context
#     }
#     return render(request, 'mobiledetails.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # تنظیم is_active به صورت خودکار
            user.is_staff = True  # تنظیم is_staff به صورت خودکار
            user.date_joined = datetime.now()  # تنظیم تاریخ ثبت نام به صورت خودکار
            user.save()
            can_list = [
                'Can add mobile',
                'Can change mobile',
                'Can view mobile',
                'Can delete mobile'
            ]
            for can in can_list:
                try:
                    permission = Permission.objects.get(name=can)
                    user.user_permissions.add(permission)
                except Permission.DoesNotExist:
                    print(f'Permission with name "{can}" does not exist.')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=username, password=raw_password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                return redirect('login')  # تغییر مسیر به صفحه اصلی پس از ثبت‌نام
            else:
                # اگر احراز هویت موفق نبود
                return render(request, 'signup.html', {'form': form, 'error_message': 'Authentication failed.'})
        else:
            # اگر فرم معتبر نبود
            return render(request, 'signup.html',
                          {'form': form, 'error_message': 'Form is not valid. Please correct the errors.'})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = True
#             user.is_staff = True
#             user.date_joined = datetime.now()
#             user.save()
#
#             #permissions
#             content_type = ContentType.objects.get_for_model(User)
#             permissions = Permission.objects.filter(content_type=content_type, codename__in=['Can add mobile', 'Can change mobile', 'Can view mobile','Can delete mobile'])
#             for perm in permissions:
#                 user.user_permissions.add(perm)
#
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login')
#         else:
#             form = CustomUserCreationForm()
#         return render(request, 'signup.html', {'form': form})


# @csrf_exempt
# def Brand_Name(request):
#     if request.user.is_authenticated:
#         if request.method == 'GET':
#             forms = Mobile.objects.all()
#             return render(request, 'signup.html', {'forms': forms})
#
#         if request.method == 'POST':
#             forms = ModelForm(request.POST)
#             if not forms.is_valid():
#                 return HttpResponse('data is not valid')
#             model = forms.cleaned_data['model']
#             price = forms.cleaned_data['price']
#             Mobile.objects.create(model, price)
#             return HttpResponse(f"model succesfully posted!: {model=}")
#         return render(request, 'forbidden.html')
#         # return HttpResponse("<h1>Error 404</h1> "
#         #                     " <h2>page not found</h2>")
#     return render(request, 'forbidden.html', context={})


# @csrf_exempt
# def model_detail(request):
#     if request.method == 'GET':
#         form = ModelForm()
#         return render(request, 'model_detail.html', {'models_form': form})
#
#     if request.method == 'POST':
#         form = ModelForm(request.POST)
#         print("print2", form)
#         if not form.is_valid():
#             return HttpResponse(form.errors)
#
#         model = form.cleaned_data['model']
#         print("print3", model)
#         Mobile.objects.create(model=model)
#         return HttpResponse(f"model created : {model=}")
#
#     return HttpResponse("<h1>Error 404</h1> "
#                         " <h2>page not found</h2>")
# model = Mobile.objects.get(id=model_id)
# return render(request, 'model_detail.html', {'models': model})


# @csrf_exempt
# def mobile_detail(request):
#     if request.user.is_authenticated:
#         if request.method == 'GET':
#             form = ModelForm()
#             return render(request, 'model_detail.html', {'forms': form})
#
#         if request.method == 'POST':
#             form = ModelForm(request.POST)
#             if not form.is_valid():
#                 return render(request, 'model_detail.html', {'forms': form})
#             #     model = form.cleaned_data['model']
#             #     Mobile.objects.create(model=model)
#             #     return HttpResponse(f'author created: {model}')
#             mobile = Mobile()
#             mobile.model = form.cleaned_data['model']
#             mobile.brand = form.cleaned_data['brand']
#             # nationality = form.cleaned_data['nationality']
#             # photos = form.cleaned_data['photos']
#             # Mobile.objects.create(model=model, brand=brand)
#             return HttpResponse(f"model created:{mobile}")
#         return HttpResponse("method not allowed")
#     return render(request, 'forbidden.html', context={})


# def model_detail(request):
#     if request.method == 'GET':
#         form = ModelForm()
#         return render(request, 'model_detail.html', {'forms' : form})
#     if request.method == 'POST':
#         form = ModelForm(request.POST)
#         if form.is_valid():
#             mobile = Mobile()
#             mobile.model = form.cleaned_data['model']
#             mobile.save()
#             return HttpResponse(f"is done!")
#         return HttpResponse("error raised")


def login(request):
    if request.method == 'GET':
        forms = AuthenticationForm()
        context = {'forms': forms}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        context = {'forms': form}
        if not form.is_valid():
            return render(request, 'login.html', context)
        # user = form.get_user()
        # pre_login(request, user)
        # return redirect('mobiles')
        user = form.get_user()
        auth_login(request, user)  # استفاده از auth_login برای ورود کاربر
        if not Cart.objects.filter(user=user).exists():
            Cart.objects.create(user=user)
        messages.success(request, f"خوش آمدید، {user.first_name} {user.last_name}!")
        return redirect('mobiles')
    return render(request, 'login.html', {'forms': AuthenticationForm()})


# def logins(request):
#     if request.method == 'GET':
#         form = AuthenticationForm()
#         return render(request, 'login.html',{'forms': form})
#     elif request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if not form.is_valid():
#             return render(request, 'login.html',{'forms': form})
#
#         user = form.get_user()
#         login(request, user)
#         return HttpResponse('you have logged in')
# @login_required(login_url='/login/')
# def register(request):
#     if request.method == 'GET':
#         form = UserCreationForm()
#         context = {'forms': form}
#         return render(request, 'register.html', context)
#
#     elif request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if not form.is_valid():
#             context = {'forms': form}
#             return render(request, 'brandpage.html', context)
#
#         form.save()
#         users = User.objects.all()
#         context = {'users': users}
#         return render(request, 'model_detail.html', context)
#
#     return HttpResponse('method not allowed')


def logout(request):
    if request.method == 'GET' and request.user.is_authenticated:
        pre_logout(request)
        return redirect('login')
        # return HttpResponse("you have logged out :'(")
    # return redirect('login')
    return render(request, 'forbidden.html', context={})


def search(request):
    query = request.GET.get('s', None)
    results = []
    if query is not None:
        #     results = Mobile.objects.filter(model__icontains=query)
        # elif query:
        results = Mobile.objects.filter(brand__name__icontains=query) or Mobile.objects.filter(model__icontains=query)
        return render(request, 'brandpage.html', {'mobiles': results})
    else:
        return render(request, 'brandpage.html', {'mobiles': results})


# class CommentView(View):
#     def get(self, request, *args, **kwargs):
#         form = ExtendedCommentForm()
#         comments = ExtendedComment.objects.all()  # نمایش تمام کامنت‌ها
#         return render(request, 'comments.html', {'form': form, 'comments': comments})
#
#     def post(self, request, *args, **kwargs):
#         form = ExtendedCommentForm(request.POST, content_type='some_type', object_pk='some_pk')
#         if form.is_valid():
#             form.save()
#             return redirect('comments')  # بازگشت به صفحه‌ی نمایش کامنت‌ها
#         comments = ExtendedComment.objects.all()  # نمایش تمام کامنت‌ها
#         return render(request, 'comments.html', {'form': form, 'comments': comments})


# @login_required
# def add_comment(request, object_id):
#     content_type = ContentType.objects.get_for_model(ExtendedComment)
#     if request.method == 'POST':
#         form = ExtendedCommentForm(request.POST, content_type=content_type, object_pk=object_id)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.commented_by = request.user
#             comment.save()
#             return redirect('mobiledetails', object_id=object_id)
#     else:
#         form = ExtendedCommentForm(content_type=content_type, object_pk=object_id)
#     return render(request, 'mobiledetails.html', {'form': form, 'object_id': object_id})


# @login_required
# def add_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.commented_by = request.user
#             comment.save()
#             return redirect('mobiledetails')  # Redirect to the brand page or any desired page
#     else:
#         form = CommentForm()
#
#     return render(request, 'mobiledetails.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # برای به‌روزرسانی session بعد از تغییر پسورد
            return redirect('password_change_done')
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})


@login_required
def password_change_done(request):
    return render(request, 'password_change_done.html')


@login_required
def user_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            item = get_object_or_404(CartItem, id=item_id, cart=cart)
            item.delete()
            return redirect('user_cart')
    cartitem_set = cart.cartitem_set.all()
    total_price = cart.get_total_price()
    context = {
        'cart': cart,
        'user': request.user,
        'cartitem_set': cartitem_set,
        'total_price': total_price
    }
    return render(request, 'register.html', context)
# @login_required
# def user_cart(request):
#     cart = get_object_or_404(Cart, user=request.user)
#     # cartitem_set = CartItem.objects.all()
#     user = request.user
#     cartitem_set = cart.cartitem_set.all()
#     total_price = cart.get_total_price()
#     context = {
#         'cart': cart,
#         'user': user,
#         'cartitem_set': cartitem_set,
#         'total_price': total_price
#     }
#     return render(request, 'register.html', context)


def inventory(request):
    mobiles_with_model = Mobile.objects.exclude(model='')  # موبایل‌هایی که مدل دارند
    if request.method == 'POST':
        inventory_form = InventoryForm(request.POST)
        if inventory_form.is_valid():
            model_name = inventory_form.cleaned_data['model']
            stock = inventory_form.cleaned_data['stock']
            try:
                mobile = Mobile.objects.get(model=model_name)
                mobile.stock = stock
                mobile.save()
            except Mobile.DoesNotExist:
                inventory_form.save()
            return redirect('inventory_success')  # مسیر به صفحه موفقیت یا لیست انبار
    else:
        inventory_form = InventoryForm()

    context = {
        'inventory_form': inventory_form,
        'mobiles_with_model': mobiles_with_model,
    }
    return render(request, 'test.html', context)
# def inventory(request):
#     if request.method == 'POST':
#         inventory_form = InventoryForm(request.POST)
#         if inventory_form.is_valid():
#             inventory_form.save()
#             return redirect('inventory_success')  # مسیر به یک صفحه موفقیت یا لیست انبار
#     else:
#         inventory_form = InventoryForm()
#
#     context = {
#         'inventory_form': inventory_form,
#     }
#     return render(request, 'test.html', context)
# def inventory(request):
#     if request.method == 'POST':
#         inventory_form = InventoryForm()


@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    mobile_id = request.data.get('mobile_id')
    quantity = request.data.get('quantity', 1)

    try:
        mobile = Mobile.objects.get(id=mobile_id)
    except Mobile.DoesNotExist:
        return Response({"error": "Mobile not found"}, status=status.HTTP_404_NOT_FOUND)

    if mobile.stock < quantity:
        return Response({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST)

    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, mobile=mobile, defaults={'quantity': quantity})

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    mobile.stock -= quantity
    mobile.save()

    return Response({"message": "Item added to cart"}, status=status.HTTP_200_OK)