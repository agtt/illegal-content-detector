from django.shortcuts import render, HttpResponse
from .models import Keyword


def index(request):
    keywords = Keyword.objects.filter(status=1)  # Get Active Status
    for keyword in keywords:
        for channel in keyword.channels.all():
            print(channel)
    return HttpResponse('OK')
