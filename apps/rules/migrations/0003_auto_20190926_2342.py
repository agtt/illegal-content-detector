# Generated by Django 2.2.5 on 2019-09-26 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0002_rule_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='page',
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
    ]
