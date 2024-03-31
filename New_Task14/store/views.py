from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Address
from django.shortcuts import redirect



def user_list(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        address = Address.objects.all()
        context = {'users': users, 'address': address}

        return render(request, 'user_list.html', context)
    return HttpResponse("you must login first")


@login_required(login_url='/login/')
def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {'forms': form}
        return render(request, 'register.html', context)

    elif request.method=='POST':
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            context = {'forms': form}
            return render(request, 'user_list.html', context)

        form.save()
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'user_list.html', context)

    return HttpResponse('method not allowed')



def logins(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html',{'forms': form})
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'login.html',{'forms': form})

        user = form.get_user()
        login(request, user)
        return HttpResponse('you have logged in')

    return HttpResponse('you were wrong!')

@login_required(login_url='/login/')
def logsout(request):
    if request.method == 'GET' and request.user.is_authenticated:
        logout(request)
        return HttpResponse("you have logged out :'(")
    return redirect('login')



# def logins(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return HttpResponse('Login completed!')
#         return HttpResponse('Wrong password/username')
#
#     return HttpResponse('Please login with post method')