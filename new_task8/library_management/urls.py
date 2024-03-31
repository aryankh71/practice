from django.urls import path

from library_management import views

urlpatterns = [
    path('booklist/', views.list_create_tasks, name='list_create_tasks')
]