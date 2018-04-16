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
        queryset = Dataset.objects.all()
        serializer = DataSetSerializer(queryset, many=True)
        return Response(serializer.data)
        
        
    def create(self, request):
        serializer = DataSetSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(data=serializer.data)
        return ResponseHandler(data=serializer.errors)

 