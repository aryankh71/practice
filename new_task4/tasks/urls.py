from django.urls import path

from .views import list_create_tasks, count_tasks, movie_name, delete_task

urlpatterns = [
    path('tasks/', list_create_tasks),
    path('tasks/count/', count_tasks),
    path('movie/', movie_name),
    path('<int:task_id>/', delete_task)

]
