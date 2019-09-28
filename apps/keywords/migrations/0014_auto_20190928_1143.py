# Generated by Django 2.2.5 on 2019-09-28 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0004_auto_20190926_2342'),
        ('keywords', '0013_auto_20190928_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='rules',
        ),
        migrations.AddField(
            model_name='keyword',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keyword_rule', to='rules.Rule', verbose_name='Rule'),
        ),
    ]
