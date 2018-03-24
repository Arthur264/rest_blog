# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, default=1)
    body = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'comment'