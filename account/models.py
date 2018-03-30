# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_blocked = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        db_table = 'user'
