# Generated by Django 3.1.4 on 2020-12-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0005_comment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
