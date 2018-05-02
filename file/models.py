# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from helpers.models import BaseModel
from django.db import models
from storage.image_storage import ImageStorage
# Create your models here.

class File(BaseModel):
    name = models.CharField(max_length=200)
    filename = models.ImageField(storage=ImageStorage())
    mime = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'file'

    def __str__(self):
        return self.name