from django.contrib import admin
from django.urls import include, path

from .views import MusicianListView, AlbumDetailView

urlpatterns = [
    path('musician/', MusicianListView.as_view(),name='musician-list'),
    # path('albums/', AlbumDetailView.as_view()),
]