from django.db.utils import IntegrityError
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from .filter import PostFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .pagination import PostLimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.forms.models import model_to_dict

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = PostFilter
    permission_classes = ( IsAuthenticated, )
    search_fields = ('title',)
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = PostLimitOffsetPagination
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer_context = {
            'request': request,
        }
        serializer = PostSerializer(data=data, context=serializer_context, many=False)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                # result = {i:model_to_dict(post)[i] for i in model_to_dict(post) if i!='image'}
                # result["image"] = []
                # for k in model_to_dict(post)['image']:
                #     k = model_to_dict(k)
                #     k.filename = k.filename.name
                #     result["image"].append(k)
                # print(result)
                return Response(serializer.data)
            except IntegrityError as e:
                return Response({"error": e})
        return Response(serializer.errors)

    def retrieve(self, request, slug=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer.add_visited()
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = ( IsAuthenticated, )

    def get_queryset(self):
        return Category.objects.all()
