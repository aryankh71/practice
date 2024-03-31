from django.http import HttpResponse


# def sad(request, name):
#     return HttpResponse("Nobody likes you, {}!".format(name))

def sad(request, name):
    return HttpResponse('my name is {}'.format(name))


# def Sad(request):
#     name = "Mohammad"
#     response = f"Nobody likes you, {name}!"
#     return HttpResponse(response)


# def happy(request, name, times):
#     return HttpResponse(("you are great, {} :)\n".format(name)) * times)


# def Happy(request):
#     name = 'Mohammad'
#     response = f'You are great, {name} :)<br>You are great, {name} :)'
#     return HttpResponse(response)
#
#
# def Happiness(request):
#     name = 'Maryam'
#     response = f'You are great, {name} :)<br>You are great, {name} :)<br>You are great, {name} :)<br>You are great, {name} :)'
#     return HttpResponse(response)
