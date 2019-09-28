from django.contrib import admin
from .models import *

admin.site.register(Keyword)
admin.site.register(Example)
admin.site.register(Whitelist)
admin.site.register(Blacklist)
admin.site.register(Website)
