from .models import Comment
from posts.models import Post
from users.serializers import UserSerializer
from django.forms.models import model_to_dict
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
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

