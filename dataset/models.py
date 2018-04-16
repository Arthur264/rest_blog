# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from storage.file_storage import FileStorage

# Create your models here.

class Dataset(models.Model):
    file = models.FileField(storage=FileStorage(),  max_length=500)
    
    class Meta:
        db_table = "dataset"