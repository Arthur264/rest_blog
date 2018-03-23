from .serializers import PostSerializer
from .models import Post
from .filter import PostFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = PostFilter
    search_fields = ('title',)

    def get_queryset(self):
        # return True
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.FILES)
        return Response(request.POST)

    # def perform_create(self, serializer):
    #     print (self)
    #     return True