from rest_framework import serializers
from rest_framework import filters

from .models import *


class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

        def to_internal_value(self, value):
            import datetime
            return datetime.datetime.fromtimestamp(int(value))

class CpuSerializer(serializers.ModelSerializer):
    router = serializers.PrimaryKeyRelatedField(queryset=Router.objects.all())
    time = UnixEpochDateField() 

    class Meta:
        model = Cpu
        fields = ('id', 'time', 'utilization', 'url', 'router')


class MemorySerializer(serializers.ModelSerializer):
    router = serializers.PrimaryKeyRelatedField(queryset=Router.objects.all())

    class Meta:
        model = Memory
        fields = ('id', 'time', 'utilization', 'url', 'router')


class RouteCountSerializer(serializers.ModelSerializer):
    vpn = serializers.PrimaryKeyRelatedField(queryset=Vpn.objects.all())
    time = UnixEpochDateField() 

    class Meta:
        model = RouteCount
        fields = ('id', 'time', 'count', 'url', 'vpn')


class VpnSerializer(serializers.ModelSerializer):
    numroutes = RouteCountSerializer(many = True, read_only = True)
    filter_fields = ('router')

    class Meta:
        model = Vpn
        fields = ('id', 'name', 'url', 'router', 'route_target', 'import_target', 'numroutes')


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface


class RouterSerializer(serializers.ModelSerializer):
    #    cpus = CpuSerializer(many = True, read_only = True)
    memorys = MemorySerializer(many = True, read_only = True)
    interfaces = InterfaceSerializer(many = True, read_only = True) 
    #vpns = VpnSerializer(many = True, read_only=True)

    class Meta:
        model = Router
        fields = ('id', 'name', 'memorys', 'interfaces', 'updated_at', 'url')
