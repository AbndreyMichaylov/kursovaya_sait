# Generated by Django 3.0.8 on 2020-12-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0009_auto_20201224_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default='05:10'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default='05:10'),
        ),
    ]
