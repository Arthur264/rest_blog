# from rest_framework import filters
from posts.models import Post
import django_filters


class PostFilter(django_filters.FilterSet):
    # draft = django_filters.BooleanFilter()
    publish = django_filters.DateFilter()
    class Meta:
        model = Post
        fields = {
            'publish': ['exact', 'lte', 'gte'],
            'user': ['exact'],
            'slug': ['exact'],
            'draft': ['exact']
        }
