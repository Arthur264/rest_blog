from .models import Post
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail')
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'body', 'slug', 'image', 'user', 'draft', 'publish')
        read_only_fields = ('id', 'slug', 'user', 'publish', 'url')
        write_only_fields = ('title', 'body', 'image', 'draft')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    def get_user(self, obj):
        return dict(id=obj.user.id, username=obj.user.username, email=obj.user.username)
