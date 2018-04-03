"""rest_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from posts.views import PostViewSet
from account.views import AuthViewSet
from users.views import UserViewSet
from comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'users', UserViewSet, base_name='user')
router.register(r'posts', PostViewSet, base_name='posts')
router.register(r'comment', CommentViewSet, base_name='comment')

# Wire up our
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls, namespace='app')),
]
    
    
