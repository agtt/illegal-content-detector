# Generated by Django 2.2.5 on 2019-09-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0004_keyword_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Video'), (2, 'Text')], default=1, null=True),
        ),
    ]
