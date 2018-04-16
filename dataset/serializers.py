from .models import Dataset
from rest_framework import serializers


class DataSetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dataset
        fields = ('id', 'file')

