from .models import Post, Category, PostVisited
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    image = serializers.ImageField(required=False)
    # url = serializers.HyperlinkedIdentityField(view_name='app:post-detail', lookup_field='pk')
    permission_classes = [IsAuthenticated]
    comment = serializers.SerializerMethodField()
    visited = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'slug', 'image', 'user', 'draft', 'publish', 'category', 'comment', 'visited')
        read_only_fields = ('id', 'slug', 'user', 'publish', 'category', 'comment', 'visited')
        write_only_fields = ('title', 'body', 'image', 'draft',)
        lookup_field = 'slug'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    def get_comment(self, obj):
        result = []
        for comment in obj.comment_set.all()[:5]:
            obj = dict()
            obj['id'] = comment.id
            obj['body'] = comment.body
            obj['parent'] = comment.parent
            result.append(obj)
        return result

    def get_visited(self, obj):
        return PostVisited.objects.filter(post=obj.id).count()

    def add_visited(self):
        try:
            visited = PostVisited(user_id=self.data["user"]["id"], post_id=self.data["id"])
            visited.save()
            return True
        except Exception as e:
            return False

    def get_user(self, obj):
        return dict(id=obj.user.id, username=obj.user.username, email=obj.user.username)
