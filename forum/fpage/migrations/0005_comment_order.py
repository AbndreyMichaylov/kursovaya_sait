# Generated by Django 3.1.4 on 2020-12-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0004_auto_20201219_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
