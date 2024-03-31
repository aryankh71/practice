from django.http import HttpResponse
from django.db.models import Max, Min
from .models import Book, Author
from .render import render_to_readable_output
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import AuthorForm

# def book_list(request):
#     min_price = request.GET.get('min_price') or 0
#     print("print==min: ", min_price)
#     # Other query parameters
#     max_price = request.GET.get('max_price', 'all')
#     print("print==max: ", max_price)
#     author = request.GET.get('author', 'all')
#     print("author: ", author)
#     name = request.GET.get('name', '')
#     print("name: ", name)
#     # author = Book.objects.values('author')
#     # name = Book.objects.values('name')
#     # return HttpResponse(f'name: {name} & author{author}')
#
#     # fill `.filter()` with query parameters
#     all_books = Book.objects.filter(price__gte=min_price, price__lte=max_price,author__icontains=author, name__icontains=name)
#     print('print', all_books)
#
#     rendered_string = render_to_readable_output(all_books)
#     return HttpResponse(rendered_string)


def book_list(request):
    min_price = request.GET.get('min_price') or 0
    # Other query parameters
    max_price = request.GET.get('max_price') or Book.objects.aggregate(max=Max('price')).get('max')
    author = request.GET.get('author', 'all')
    name = request.GET.get('name', '')

    # fill `.filter()` with query parameters
    all_books = Book.objects.filter(name__icontains=name, author__icontains=author, price__lte=max_price,
                                    price__gte=min_price)

    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)


@csrf_exempt
def authors(request):
    if request.method == 'GET':
        author_list = Author.objects.all()
        context = {
            "authors": author_list
        }
        return render(request, 'author_list.html', context)
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        # data = form.data['name'] ----> hamoon kare request.POST ro anjam mide va data tamiz shode dakhelesh nist
        if not form.is_valid():
            return HttpResponse('data is not valid')

        name = form.cleaned_data['name']
        # vaghticleaned_data ro seda mizanim hata customhaye marboot be form ham ejra mikone
        Author.objects.create(name=name)
        return HttpResponse(f'author created: {name=}')

    return HttpResponse('method not allowed')


@csrf_exempt
def new_author(request):
    if request.method == 'GET':
        form = AuthorForm()
        return render(request, 'new_author.html', {'author_form': form})

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render(request, 'new_author.html', {'author_form': form})

        name = form.cleaned_data['name']
        Author.objects.create(name=name)
        return HttpResponse(f'author created: {name=}')

    return HttpResponse('<h1> method not allowed </h1>')
    # author = Author.objects.get(id=author_id)
    # context = {
    #     'authors': author
    # }
    # return render(request, 'new_author.html', context)
    #





# def index(request):
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
#     books = Book.objects.filter(


#         price__gte=min_price, price__lte=max_price
#     ).values_list('name', flat=True)
#     # return HttpResponse(f'your request has been accepted'.join(map(str, books)))
#     return HttpResponse(f'this is your book: {books}')


def booklist(request):
    books = Book.objects.all().values_list('name', flat=True)
    return render(request, 'booklist.html', {"books": books})
