from django.shortcuts import render, HttpResponse
from .models import Keyword


def index(request):
    keywords = Keyword.objects.filter(status=1)  # Get Active Status
    for keyword in keywords:
        for example in keyword.examples.all():
            name = f'{keyword.name} {example}'
            print(name)
    return HttpResponse('OK')
