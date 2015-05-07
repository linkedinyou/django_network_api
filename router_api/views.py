from django.shortcuts import render
from django.http import HttpResponse
import django_filters

from rest_framework import routers, serializers, viewsets, generics, filters

from .models import *
from .serializers import *

class CpuFilter(django_filters.FilterSet):
    date = django_filters.DateTimeFilter(name='time', lookup_type='gte')

    class Meta:
        model = Cpu
        filter_fields = ['date', 'router']

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object

class RouterViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer
    filter_fields = ('name',)

class VpnViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    queryset = Vpn.objects.all()
    serializer_class = VpnSerializer
    filter_fields = ('router',)

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all().order_by('time')
    serializer_class = CpuSerializer
    filter_class = CpuFilter

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all().order_by('time')
    serializer_class = MemorySerializer

class RouteCountViewSet(viewsets.ModelViewSet):
    queryset = RouteCount.objects.all().order_by('time')
    serializer_class = RouteCountSerializer
