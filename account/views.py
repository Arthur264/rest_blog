# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import User
from account.serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = User

    def create(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def list(self, request):
        users = User.objects.values('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')
        # serializer = UserSerializer(users, many=True, required='id')
        return Response(users)
