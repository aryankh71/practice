from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from library_management.models import Book
from django.http import HttpResponse


# def booklist(request):
#     books = Book.objects.all()
#     return render(request, 'booklist.html', context = {'books': books})


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        added_task = request.POST.get('title')
        new_task = Book(title=added_task)
        new_task.save()
        return HttpResponse(f"Task Created: '{added_task}'")

    elif request.method == 'GET':
        return HttpResponse(f"it works")