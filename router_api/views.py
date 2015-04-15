from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import routers, serializers, viewsets

from .models import *
from .serializers import *

class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer


class VpnViewSet(viewsets.ModelViewSet):
    queryset = Vpn.objects.all()
    serializer_class = VpnSerializer


class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all().order_by('time')
    serializer_class = CpuSerializer


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all().order_by('time')
    serializer_class = MemorySerializer


class RouteCountViewSet(viewsets.ModelViewSet):
    queryset = RouteCount.objects.all().order_by('time')
    serializer_class = RouteCountSerializer
