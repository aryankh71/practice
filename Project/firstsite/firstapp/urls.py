from django.urls import path
# from * import views
from .views import signup_view
from .views import sayhello
from .views import index
# from .views import signup_view
urlpatterns = [
    path('', signup_view),
    path('', sayhello),
    path('', index)
]
