from helpers.response import ResponseHandler
from .serializers import DataSetSerializer
from .models import Dataset
from rest_framework.response import Response
from rest_framework import viewsets, permissions

class DatasetViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DataSetSerializer
    
    
    def get_queryset(self):
        return Dataset.objects.all()


    def list(self, request):
        queryset = Dataset.objects.filter(user=request.user.id)
        serializer = DataSetSerializer(queryset, many=True)
        return Response(serializer.data)
        
        
    def create(self, request):
        serializer_context = {
            'request': request,
        }
        serializer = DataSetSerializer(data=request.data, context=serializer_context, many=False)
        if serializer.is_valid():
            name = request.FILES['file'].name.split('.')[0]
            serializer.save(user=request.user, name=name, type=request.FILES['file'].content_type)
            return ResponseHandler(data=serializer.data)
        return ResponseHandler(data=serializer.errors)

 