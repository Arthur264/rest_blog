# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from helpers.models import BaseModel
from account.models import User
from posts.models import Post


# Create your models here.

class Comment(BaseModel):
    user = models.ForeignKey(User, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.body[:15]

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
