# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from storage.file_storage import FileStorage
from users.models import User
from helpers.models import BaseModel
# Create your models here.

class Dataset(BaseModel):
    user = models.ForeignKey(User)
    type = models.CharField(null=True, blank=True, max_length=50)
    file = models.FileField(storage=FileStorage(),  max_length=500)
    name = models.CharField(null=True, blank=True, max_length=200)
    class Meta:
        db_table = "dataset"
        ordering = ['-update']
        