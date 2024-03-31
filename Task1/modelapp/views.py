from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import Book

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def User(request):
    Book = Book(name ="aryan")