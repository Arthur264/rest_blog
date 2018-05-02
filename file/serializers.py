from .models import File
from rest_framework import serializers


class FileSerializer(serializers.HyperlinkedModelSerializer):
    filename = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = File
        fields = ('id', 'name', 'filename')
        
    def get_queryset(self):
        return File.objects.all()
