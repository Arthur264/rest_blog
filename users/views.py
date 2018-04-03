# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from account.permissions import IsAdminOrIsSelf


# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    class Meta:
        model = User

    def get_queryset(self):
        return User.objects.all()

    def create(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def list(self, request):
        users = User.objects.values('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'password')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def update(self, request):
        return Response(request)

    def retrieve(self, request, username):
        data = User.objects.get(username=username)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf], url_path='change-password')
    def set_password(self, request):
        pass
