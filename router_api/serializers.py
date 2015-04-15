from rest_framework import serializers

from .models import *

class CpuSerializer(serializers.HyperlinkedModelSerializer):
    router = serializers.PrimaryKeyRelatedField(queryset=Router.objects.all())
    class Meta:
        model = Cpu
        fields = ('id', 'time', 'utilization', 'url', 'router')


class MemorySerializer(serializers.ModelSerializer):
    router = serializers.PrimaryKeyRelatedField(queryset=Router.objects.all())
    class Meta:
        model = Memory
        fields = ('id', 'time', 'utilization', 'url', 'router')


class RouteCountSerializer(serializers.HyperlinkedModelSerializer):
    vpn = serializers.PrimaryKeyRelatedField(queryset=Vpn.objects.all())

    class Meta:
        model = RouteCount
        fields = ('id', 'time', 'count', 'url', 'vpn')
        

class VpnSerializer(serializers.HyperlinkedModelSerializer):
    num_routes = RouteCountSerializer(many = True, read_only = True)

    class Meta:
        model = Vpn
        fields = ('id', 'name', 'url', 'router', 'route_target', 'import_target', 'num_routes')


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface


class RouterSerializer(serializers.HyperlinkedModelSerializer):
    cpus = CpuSerializer(many = True, read_only = True)
    memorys = MemorySerializer(many = True, read_only = True)
    interfaces = InterfaceSerializer(many = True, read_only = True) 
    vpns = VpnSerializer(many = True, read_only=True)

    class Meta:
        model = Router
        fields = ('id', 'name', 'cpus', 'memorys', 'interfaces', 'vpns', 'updated_at', 'url')
