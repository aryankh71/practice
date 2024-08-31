from django.urls import path
from .views import Mobile_Post
# from .views import Brand_Name
# from .views import mobile_detail
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('mobiles/',Mobile_Post, name='mobiles'),
    # path('comments/', CommentView.as_view(), name='comments'),
    path('details/<int:id>/', Mobile_Details, name='mobiledetails'),
    # path('brands/', Brand_Name, name='brands'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('register/', register, name='register'),
    path('search/',search, name='search'),
    path('signup/', signup, name='signup'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-change-done/', views.password_change_done, name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('cart/', views.user_cart, name='user_cart'),
    path('invent/', inventory, name='inventory'),
    path('api/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('apiview/', MobileListAPIView.as_view(), name='mobilelist'),
]