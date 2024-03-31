from django.urls import path

from web.views import *


urlspatterns = [
    path('sad/<str:name>/', sad),
]


# urlspatterns = [
#     path('happy/<str:name>/<int:times>/', happy),
#     path('sad/<str:name>/', sad),
# ]