# Generated by Django 2.2.5 on 2019-09-28 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0010_website'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blacklist',
        ),
        migrations.DeleteModel(
            name='Whitelist',
        ),
    ]
