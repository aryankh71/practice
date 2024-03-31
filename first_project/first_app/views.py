from django.shortcuts import render
from django.shortcuts import HttpResponse
from first_app.models import *



def signup_view(request):
    return HttpResponse('signup Completed')


def welcome(request):
    return HttpResponse(f"<h1 dir='rtl'>خوش آمد</h1>")


# Cannot assign "'alikhodakhah'": "Post.writer" must be a "User" instance.
def Posts(request, content, writer):
    return HttpResponse("content={} </br> writer={}".format(content, writer))


def Persons(request):
    first = Person(name='aryan')
    lastname = Person(family='khodakhah')
    year = Person(age=30)
    flag = Person(country='Iran')
    return HttpResponse(f"<h1>name={first.name}&family={lastname.family}&age={year.age}&country={flag.country}</h1>")


def Indexes(request, username, email):
    response = f"name: {username} </br> email: {email}"
    return HttpResponse(response)


def Index(request, username, gender, times):
    return HttpResponse(f"username = {username} </br> gender = {gender}</br>" * times)

    # user = User(username='alikhodakhah')
    # get = User(email='aryankhodakhah@gamil.com')
    # response = f"<title>name={user.username}&email={get.email}</title>"
    # return HttpResponse(response)


# def msg_sender(request):
#     msg = "Hello world"
#     return HttpResponse(msg)