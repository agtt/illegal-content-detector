from django.shortcuts import render, HttpResponse
from .models import Keyword
from apps.reports.models import Report


def index(request):
    keywords = Keyword.objects.filter(status=1)  # Get Active Status
    for keyword in keywords:
        for example in keyword.examples.all():
            name = f'{keyword.name} {example}'
            for channel in keyword.channels.all():
                Report.objects.create(name=name, example=example, channel=channel, keyword=keyword)
            print(name)
    return HttpResponse('OK')
