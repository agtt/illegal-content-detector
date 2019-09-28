from django.db import models
from apps.channels.models import Channel

STATUS = (
    (0, 'WAITING'),
    (1, 'COMPLETED'),
    (2, 'CRAWLER'),
)


class Report(models.Model):
    url = models.URLField(blank=True, null=True)
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE,
                                related_name="report_channel",
                                verbose_name="Channel")
    date_added = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.url
