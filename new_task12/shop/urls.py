from django.urls import path
from .views import show_people, submit_persons

urlpatterns = [
    path('people/', show_people),
    path('submit/', submit_persons),
]
