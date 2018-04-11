# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .permissions import IsAdminOrIsSelf
from users.models import User
from rest_framework import status
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token


# Create your views here.

class AuthViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    @list_route(methods=['post'], permission_classes=[IsAdminOrIsSelf], url_path='change-password')
    def set_password(self, request):
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'], url_path='login')
    def login(self, request):
        print(request.auth)
        return Response({"test": request.user.auth_token})

    @list_route(methods=['post'], url_path='register')
    def register(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'], permission_classes=[IsAdminOrIsSelf], url_path='logout')
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    @list_route(methods=['get'], permission_classes=[IsAdminOrIsSelf], url_path='token')
    def token(self, request):
        u = User.objects.get(username=request.user.username)
        token, created = Token.objects.get_or_create(user=u)
        request.user.token = token.key
        return Response({"token": token.key})
