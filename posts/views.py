from django.db.utils import IntegrityError
from .serializers import PostSerializer
from .models import Post
from .filter import PostFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .pagination import PostLimitOffsetPagination
from imgur.client import client


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = PostFilter
    search_fields = ('title',)
    pagination_class = PostLimitOffsetPagination
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        # fd = client.upload(request.FILES)
        # return Response(fd)
        # print (data)
        serializer_context = {
            'request': request,
        }
        serializer = PostSerializer(data=data, context=serializer_context)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError:
                return Response({"error": "slug empty"})
        return Response(serializer.errors)


def retrieve(self, request, slug=None):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    serializer.add_visited()
    return Response(serializer.data)
