# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import storage.image_storage


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180414_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, storage=storage.image_storage.ImageStorage(), upload_to=b''),
        ),
    ]
