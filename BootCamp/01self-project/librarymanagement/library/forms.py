from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='نویسنده')

    class Meta:
        model = Book
        published = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='تاریخ انتشار')
        fields = ('name', 'author', 'published', 'description', 'categories', 'price')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'write_date', 'description', 'is_alive')
