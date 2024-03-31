from django.urls import path

from .views import book_list, booklist, authors, new_author

urlpatterns = [
    path('books/', booklist),
    path('authors/', authors),
    path('new-author/', new_author),
]
