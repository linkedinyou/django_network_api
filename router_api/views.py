from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import routers, serializers, viewsets

from .models import *
from .serializers import *

class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer
