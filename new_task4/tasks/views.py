from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import logging
import requests


def list_create_tasks(request):
    if request.method == 'GET':
        return HttpResponse('\n'.join(Task.objects.all().order_by('name').values_list('name', flat=True)))


def count_tasks(request):
    if request.method == 'GET':
        return HttpResponse(f"You have '{Task.objects.count()}' tasks to do")


# def list_create_tasks(request):
#     if request.method == 'GET':
#         all_work = Task.objects.order_by('name')
#         new_line = '\n'.join(map(str, all_work))
#         # print(type(new_line)
#         return HttpResponse(new_line)
# for item in all_work:
#     return HttpResponse(item)
# list = []
# for item in all_work:
#     list.append(item)
#     return HttpResponse(list)

# "\n".join(name_score[0] + " " + name_score[1] for name_score in pairs)
# def show_todo():
#     my_list = []
#     for key, value in cal.items():
#         my_list.append((value[0], key))
#     return my_list


# def count_tasks(request):
#     if request.method == 'GET':
#         pass  # Your Code Here


# example: Task Created: 'Study for 2 hours'
# Task Created: '__Task_Name_Here__'
# def my_view(request):
#     c = {}
#     # ...
#     return render(request, "a_template.html", c)
# @csrf_exempt
# def list_create_tasks(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         return render(request, f"this", '{name:name}')
# try:
#     task = Task.objects.get(name=name)
#     return HttpResponse(f"Task Created: '{name}'")
# except ValueError:
#     return HttpResponse(f"not found :'(")
# id = request.POST.get('id'):'(
# print('print__id===>', id)
# task = Task.objects.get(id=id)
# print('print ====>', task)
# return HttpResponse(f'Task Created {task}')

@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        Task.objects.create(name=request.POST.get('task'))
        return HttpResponse(f"Task Created: '{request.POST.get('task')}'")
    else:
        return HttpResponse("it doesn't work")


@csrf_exempt
def movie_name(request, name):
    # name = Task.objects.get(name=name)
    # if name == None:
    #     name = Task.objects.create(name=request.POST.get('name'))
    #     return HttpResponse(f"esme{name.name} to jadval nabud vali man barat sakhtam")
    # print("print==>", name_id)
    # age = Task.objects.create(age=age_id)
    # name = Task.objects.create(name=name_id)
    # return HttpResponse(f"my name is {name} and my age is {age}")
    # return HttpResponse(f"ba esme man safhe baz shod \n in esm {name.name} to jadval hast")

    if request.method == 'POST':
        name = request.POST.get('name')
        if name is None:
            return HttpResponse("ino peyda nakardam")

        esm = Task.objects.create(name=name)
        return HttpResponse(f"esme {esm.name=} nabud vali barat sakhtamesh <3")
    else:
        return HttpResponse(f"nashod bazam talash kon")


# def delete(self,request,train_id=None):
#     route = get_object_or_404(Schedule, pk=train_id)
#     response = u'Successful delete route {}'.format(route.display_name())
#     route.delete()
#     return HttpResponse(response)



@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return HttpResponse(f"Task Done: '{task.name}'")
        except Task.DoesNotExist:
            return HttpResponse(f"There isn't any task with id '{task_id}'")
    else:
        return HttpResponse(f"Method not allowed. Use DELETE request.")
#         try:
#             task = Task.objects.get(id=task_id)
#             return HttpResponse(f"Task Done: '{task.name}'")
#         except Exception as e:
#             return HttpResponseRedirect("An error occurred: {}".format(str(e)), status=500)
    # else:

    #
    #     return HttpResponse(f"There isn't any task with id '{task_id}'")
    # except Exception as e:
    #     # Handle the exception
    #     return HttpResponse("An error occurred: {}".format(str(e)), status=500)

# how to change GET request to DELETE request

# @csrf_exempt
# def delete_task(request, task_id):
#     logger.debug(f"Received DELETE request for task ID: {task_id}")
#     if request.method == 'DELETE':
#         try:
#             task = Task.objects.get(id=task_id)
#             task_name = task.name
#             task.delete()
#             return JsonResponse(f"Task Done:'{task_name}'")
#         except ObjectDoesNotExist:
#             logger.error(f"No task found with ID: {task_id}")
#             return JsonResponse({'error': f"No task found with id '{task_id}'"}, status=404)
#         except Exception as e:
#             logger.error(f"An error occurred: {e}")
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         logger.error("Method not allowed")
#         return JsonResponse({'error': "Method not allowed"}, status=405)