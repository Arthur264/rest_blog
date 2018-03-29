from .models import Comment
from posts.models import Post
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')
    parent = serializers.SlugRelatedField(queryset=Comment.objects.all(), slug_field='pk', default=None)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'body', 'post', 'parent')
        read_only_fields = ('id', 'user')
        write_only_fields = ('body', 'post', 'parent')
        lookup_field = 'pk'

    def get_post(self, obj):
        return dict(id=obj.post.id, title=obj.post.title)

    def get_user(self, obj):
        return dict(id=obj.user.id, username=obj.user.username, email=obj.user.username)
