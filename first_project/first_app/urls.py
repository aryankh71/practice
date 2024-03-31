from django.urls import path
from first_app.views import welcome
from first_app.views import Index
from .views import Persons
from .views import Posts


urlpatterns = [
    path('say/welcome', welcome),
    path('Index/', Index),
    path('Interview/', Persons),
    path('Posts/', Posts),
]