from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    publish = models.DateField(auto_now=True, auto_now_add=False)
    create = models.DateField(auto_now=False, auto_now_add=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # set the slug explicitly
        super(Post, self).save(*args, **kwargs)  # call Django's save()
