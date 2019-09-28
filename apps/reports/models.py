from django.db import models
from apps.channels.models import Channel


class Report(models.Model):
    url = models.URLField(blank=True, null=True)
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE,
                                related_name="report_channel",
                                verbose_name="Channel")
