from django.http import HttpResponse


def happy(request, name, times):
    return HttpResponse(("You are great, {} :)\n".format(name)) * times)


def sad(request, name):
    return HttpResponse("Nobody likes you, {}!".format(name))
