from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views import View
from django.views.generic import ListView, DetailView

# class Musician_list(View):
#     def get(self, request):
#         musicians = Musician.objects.all().order_by('name').values_list('name', flat=True)
#         return HttpResponse(musicians)


# class MusicianListView(ListView):
#     model = Musician
#     template = 'musician_list.html'
#     # model = YourModel  # Specify the model to list
#     # template_name = 'your_app/your_model_list.html'  # Specify the template to render
#     # context_object_name = 'your_model_list'  # Specify the context variable name in the template
#     #
#     # def get_queryset(self):
#     #     # Customize queryset if needed
#     #     return YourModel.objects.filter(some_filter_condition)
#
#
# class AlbumDetailView(DetailView):
#     pass


class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    paginate_by = 1
    queryset = Musician.objects.order_by('name')


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'
    queryset = Album.objects.filter(num_stars__gte=3)