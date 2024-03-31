from django.http import HttpResponse


def happy(request, name, times):
    return HttpResponse(("you are great, {} :)\n".format(name)) * times)


def sad (request, name):
    return HttpResponse((f'nobody likes you, {name}!'))