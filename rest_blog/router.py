from posts.views import PostViewSet
from account.views import AuthViewSet
from users.views import UserViewSet
from comment.views import CommentViewSet
from dataset.views import DatasetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'users', UserViewSet, base_name='user')
router.register(r'posts', PostViewSet, base_name='posts')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'dataset', DatasetViewSet, base_name='dataset')
