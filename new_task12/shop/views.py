from django.http import HttpResponse
from django.shortcuts import render
from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)



def submit_persons(request):
    if request.method == 'GET':
        form = PersonalInformation()
        return render(request, 'new_person.html', {'forms':form})

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        if not form.is_valid():
            return render(request, 'new_person.html', {'forms':form})

        person = Person()
        person.gender = form.cleaned_data['gender']
        person.full_name = form.cleaned_data['full_name']
        person.height = form.cleaned_data['height']
        person.age = form.cleaned_data['age']
        person.save()
        return HttpResponse(person, status=201)

