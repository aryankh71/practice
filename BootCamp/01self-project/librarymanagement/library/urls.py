from django.urls import path
from .views import create_books, books_list
from .views import create_author, delete_book, edit_book


urlpatterns = [
    path('createbooks/',create_books,name='createbooks'),
    path('bookslist/', books_list, name='bookslist'),
    path('createauthor/', create_author, name='createauthor'),
    path('deletebook/<int:book_id>/', delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
]
