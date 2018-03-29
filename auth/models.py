# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'user_profile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = User.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
