from .models import Post, Category
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from auth.serializers import UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    image = serializers.ImageField(required=False)
    # url = serializers.HyperlinkedIdentityField(view_name='app:post-detail', lookup_field='pk')
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'slug', 'image', 'user', 'draft', 'publish', 'category')
        read_only_fields = ('id', 'slug', 'user', 'publish', 'category')
        write_only_fields = ('title', 'body', 'image', 'draft', )
        lookup_field = 'slug'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    def get_user(self, obj):
        return dict(id=obj.user.id, username=obj.user.username, email=obj.user.username)
