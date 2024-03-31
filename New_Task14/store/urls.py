from django.urls import path
from .views import user_list, register, logins,logsout

urlpatterns = [
    path('users/', user_list),
    path('register/', register),
    path('login/', logins, name='login'),
    path('logout/', logsout, name='logout'),
]