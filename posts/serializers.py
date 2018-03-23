from .models import Post
from rest_framework import serializers
from auth.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    # image = serializers.ImageField(max_length=None, use_url=True)
    permission_classes = [IsAuthenticated]
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'slug', 'image', 'user', 'draft', 'publish')
        read_only_fields = ('id', 'slug', 'user', 'publish')
        write_only_fields = ('title', 'body', 'image', 'draft')

    # def create(self, validated_data):
    #     pass

    def saveimage(self):
        pass