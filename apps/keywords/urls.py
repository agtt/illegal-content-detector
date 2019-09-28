from django.conf.urls import url, include, re_path
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', index),
]
