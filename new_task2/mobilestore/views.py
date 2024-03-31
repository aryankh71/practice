from django.http import HttpResponse
from .models import Mobile
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as pre_login, logout as pre_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@csrf_exempt
def Mobile_Post(request):
    if request.user.is_authenticated:
        mobile = Mobile.objects.all()
        return render(request, 'brandpage.html', {'mobiles': mobile})
    return render(request, 'forbidden.html', context={})
    # return HttpResponse("khodafez")


@csrf_exempt
def Brand_Name(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            forms = Mobile.objects.all()
            return render(request, 'signup.html', {'forms': forms})

        if request.method == 'POST':
            forms = ModelForm(request.POST)
            if not forms.is_valid():
                return HttpResponse('data is not valid')
            model = forms.cleaned_data['model']
            price = forms.cleaned_data['price']
            Mobile.objects.create(model, price)
            return HttpResponse(f"model succesfully posted!: {model=}")
        return render(request, 'forbidden.html')
        # return HttpResponse("<h1>Error 404</h1> "
        #                     " <h2>page not found</h2>")
    return render(request, 'forbidden.html', context={})

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

@csrf_exempt
def model_detail(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ModelForm()
            return render(request, 'model_detail.html', {'forms': form})

        if request.method == 'POST':
            form = ModelForm(request.POST)
            if not form.is_valid():
                return render(request, 'model_detail.html', {'forms': form})
            #     model = form.cleaned_data['model']
            #     Mobile.objects.create(model=model)
            #     return HttpResponse(f'author created: {model}')
            mobile = Mobile()
            mobile.model = form.cleaned_data['model']
            mobile.brand = form.cleaned_data['brand']
            # nationality = form.cleaned_data['nationality']
            # photos = form.cleaned_data['photos']
            # Mobile.objects.create(model=model, brand=brand)
            return HttpResponse(f"model created:{mobile}")
        return HttpResponse("method not allowed")
    return render(request, 'forbidden.html', context={})

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

        user = form.get_user()
        pre_login(request, user)
        return redirect('product')


def logout(request):
    if request.method == 'GET' and request.user.is_authenticated:
        pre_logout(request)
        return HttpResponse("you have logged out :'(")
    # return redirect('login')
    return HttpResponse('log in again')