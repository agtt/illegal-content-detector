from django.db import models
from apps.channels.models import Channel
from apps.keywords.models import Keyword, Example
from django.utils import timezone

STATUS = (
    (0, 'WAITING'),
    (1, 'COMPLETED'),
    (2, 'CRAWLER'),
)


class Report(models.Model):
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=400, blank=True, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                related_name="report_channel",
                                verbose_name="Channel")
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE,
                                related_name="report_keyword",
                                verbose_name="Keyword")
    example = models.ForeignKey(Example, on_delete=models.CASCADE,
                                related_name="report_example",
                                verbose_name="Example")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    type = models.IntegerField(choices=((1, 'LEGAL'), (2, 'ILLEGAL')), blank=True, null=True)

    def __str__(self):
        return f'{self.channel} : {self.name} - {self.url}'

    def save(self, *args, **kwargs):
        """" On save, update timestamps """
        self.updated_at = timezone.now()
        if self.status:
            self.finished_at = timezone.now()
        return super(Report, self).save(*args, **kwargs)