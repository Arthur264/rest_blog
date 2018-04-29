# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from helpers.models import BaseModel
from django.db import models
from storage.image_storage import ImageStorage
# Create your models here.

class Image(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(storage=ImageStorage())
    
    class Meta:
        db_table = 'image'

    def __str__(self):
        return self.name