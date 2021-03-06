# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0003_dataset_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='type',
            field=models.CharField(default='tes', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
