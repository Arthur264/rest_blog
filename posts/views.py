from .serializers import PostSerializer
from .models import Post
from .filter import PostFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from imgur.client import client
from  .pagination import PostLimitOffsetPagination

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = PostFilter
    search_fields = ('title',)
    pagination_class = PostLimitOffsetPagination
    # lookup_field = 'slug'


    def get_queryset(self):
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
        fd = client.upload(request.FILES)
        data = request.POST.copy()
        data['image'] = fd['data']['link']
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
