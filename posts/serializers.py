from .models import Post, Category, PostVisited
from rest_framework import serializers
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    image = serializers.ImageField(max_length=None, use_url=True)
    url = serializers.HyperlinkedIdentityField(view_name='app:posts-detail', lookup_field='slug')
    permission_classes = [IsAuthenticated]
    # comment = CommentSerializer(many=True)
    visited = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'slug', 'image', 'user', 'draft', 'publish', 'category', 'url', 'visited')
        read_only_fields = ('id', 'slug', 'user', 'publish', 'url', 'visited')
        write_only_fields = ('title', 'body', 'image', 'draft')
        lookup_field = 'slug'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    # def get_comment(self, obj):
    #     result = []
    #     for comment in obj.comment_set.all()[:5]:
    #         obj = dict()
    #         obj['id'] = comment.id
    #         obj['body'] = comment.body
    #         print (comment.parent)
    #         obj['parent'] = comment.parent
    #         result.append(obj)
    #     return result

    def get_visited(self, obj):
        return PostVisited.objects.filter(post=obj.id).count()

    def add_visited(self):
        try:
            visited = PostVisited(user_id=self.data["user"]["id"], post_id=self.data["id"])
            visited.save()
            return True
        except Exception as e:
            return False

            # def get_user(self, obj):
            #     return dict(id=obj.user.id, username=obj.user.username, email=obj.user.username)
