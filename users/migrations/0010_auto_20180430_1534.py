# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180419_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='create',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='update',
            new_name='update_at',
        ),
    ]
