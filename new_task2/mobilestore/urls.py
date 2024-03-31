from django.urls import path
from .views import Mobile_Post
from .views import Brand_Name
from .views import model_detail
from .views import login, logout


urlpatterns = [
    path('product/',Mobile_Post, name='product'),
    path('brands/', Brand_Name, name='brands'),
    path('details/', model_detail, name='details'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('register/', register, name='register'),
]