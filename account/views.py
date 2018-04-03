# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .permissions import IsAdminOrIsSelf


# Create your views here.

class AuthViewSet(viewsets.ViewSet):
    pass


@detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf], url_path='change-password')
def set_password(self, request):
    pass
