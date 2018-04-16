from helpers.response import ResponseHandler
from .serializers import CommentSerializer
from .models import Comment
from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Comment.objects.all()
    
    
    def create(self, request, *args, **kwargs):
        data = request.POST.copy()
        serializer_context = {
            'request': request,
        }
        serializer = CommentSerializer(data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(data=serializer.data)
        return ResponseHandler(error=serializer.errors)
