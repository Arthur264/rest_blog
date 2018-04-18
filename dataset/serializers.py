from .models import Dataset
from rest_framework import serializers


class DataSetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Dataset
        fields = ('id', 'user', 'file', 'type', 'name')

    
        