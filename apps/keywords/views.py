from django.shortcuts import render, HttpResponse
from .models import Keyword


def index(request):
    keywords = Keyword.objects.all()
    for val in keywords:
        print(val)
    return HttpResponse('OK')
