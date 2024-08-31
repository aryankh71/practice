from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BookForm, AuthorForm
from .models import Book
from django.db.models import Q
from django.http import HttpResponseRedirect


def create_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if not form.is_valid():
            return render(request, 'create_book.html', {'forms': form})

        form.save()
        return redirect('bookslist')
    else:
        form = BookForm()

        return render(request, 'create_book.html', {'forms': form})


def books_list(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(name__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        )

    if min_price:
        books = books.filter(price__gte=min_price)

    if max_price:
        books = books.filter(price__lte=max_price)

    if start_date:
        books = books.filter(published__gte=start_date)

    if end_date:
        books = books.filter(published__lte=end_date)

    context = {
        'books': books,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'start_date': start_date,
        'end_date': end_date
    }

    return render(request, 'bookslist.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookslist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if not form.is_valid():
            return render(request, 'edit_book.html', {'forms': form})

        form.save()
        return redirect('bookslist')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'forms': form})


def create_author(request):
    if request.method == 'POST':
        forms = AuthorForm(request.POST)
        if not forms.is_valid():
            return render(request, 'create_author.html', {'forms': forms})
        forms.save()
        return HttpResponse('Author created successfully!')

    else:
        form = AuthorForm()

        return render(request, 'create_author.html', {'forms': form})