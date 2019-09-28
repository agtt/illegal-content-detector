from django.db import models


class Day(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=300)
    page = models.IntegerField(default=1, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    days = models.ManyToManyField(Day, blank=True)

    def __str__(self):
        return self.name
