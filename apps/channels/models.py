from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=150)
    code = models.SlugField(unique=True)

    def __str__(self):
        return self.name