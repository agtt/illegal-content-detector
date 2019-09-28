from django.db import models
from apps.rules.models import Rule
from apps.channels.models import Channel

KEYWORD_TYPES = (
    (1, 'Video'),
    (2, 'Text')
)

STATUS = (
    (1, 'Active'),
    (0, 'Inactive'),
)


class Example(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Whitelist(models.Model):
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.url


class Blacklist(models.Model):
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.url


class Keyword(models.Model):
    name = models.CharField(max_length=400)
    duration = models.DurationField(null=True, blank=True)
    type = models.IntegerField(choices=KEYWORD_TYPES, default=1, blank=True, null=True)
    channels = models.ManyToManyField(Channel, blank=True)
    examples = models.ManyToManyField(Example, blank=True)
    # start_date = models.DateTimeField(null=True, blank=True)
    # end_date = models.DateTimeField(null=True, blank=True)
    rules = models.ForeignKey(Rule, null=True, blank=True, on_delete=models.CASCADE,
                              related_name="keyword_rule",
                              verbose_name="Rules")
    active = models.IntegerField(default=1, choices=STATUS)

    def __str__(self):
        return self.name
