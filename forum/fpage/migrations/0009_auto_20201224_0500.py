# Generated by Django 3.0.8 on 2020-12-24 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0008_auto_20201220_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=datetime.time(5, 0, 29, 645543)),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(default=datetime.time(5, 0, 29, 645543)),
        ),
    ]
