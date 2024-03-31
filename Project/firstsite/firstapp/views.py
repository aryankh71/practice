from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse
from .models import User

from django.http import HttpResponse
from .models import Person


# def signup_view(request, name):
#     return HttpResponse(f'<h1>{name} jan! function aval(1) faal shod<h1>')
def signup_view(request):
    person = Person(name="aryan", lname="khodakhah")
    # response = f"<p>welcome <b>{person.name} {person.lname}</b> </p>"
    response = f"<form>First name: <input/></form> \n Last name: <input/>"
    return HttpResponse(response)

print(signup_view('aryan'))


def sayhello(request):
    return HttpResponse('<p>function dovom(2) faal shod<p>')


def index(request):
    user = User(name='sajjad')
    response = f"<h1>{user.name}</h1>"
    return HttpResponse(response)