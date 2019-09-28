# Generated by Django 2.2.5 on 2019-09-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0009_blacklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Whitelist'), (1, 'Blacklist')], default=0, null=True)),
            ],
        ),
    ]