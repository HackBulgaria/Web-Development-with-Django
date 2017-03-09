from django.shortcuts import render

from .services import set_key


def add_key(request, identifier):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')

        set_key(identifier=identifier, key=key, value=value)


    return render(request, 'add_key.html')
