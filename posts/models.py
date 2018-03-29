from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from helpers.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Post(BaseModel):
    user = models.ForeignKey(User, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    body = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    publish = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # set the slug explicitly
        return super(Post, self).save(*args, **kwargs)  # call Django's save()
