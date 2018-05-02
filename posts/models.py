from __future__ import unicode_literals
from users.models import User
from django.db import models
from helpers.models import BaseModel
from django.utils.text import slugify
from storage.image_storage import ImageStorage
from file.models import File


class Category(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Post(BaseModel):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    body = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(File, related_name='image', null=True, blank=True)
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    publish = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class PostVisited(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
        db_table = 'post_visited'

