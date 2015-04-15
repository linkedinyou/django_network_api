from rest_framework import serializers

from .models import *

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ('id', 'time', 'utilization')


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ('id', 'time', 'utilization')


class RouteCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteCount
        fields = ('id', 'time', 'count')
        

class VpnSerializer(serializers.HyperlinkedModelSerializer):
    num_routes = RouteCountSerializer(many = True)

    class Meta:
        model = Vpn


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface


class RouterSerializer(serializers.HyperlinkedModelSerializer):
    cpus = CpuSerializer(many = True, read_only = True)
    memorys = MemorySerializer(many = True, read_only = True)
    interfaces = InterfaceSerializer(many = True, read_only = True) 
    vpns = VpnSerializer(many = True)

    class Meta:
        model = Router
        fields = ('id', 'name', 'cpus', 'memorys', 'interfaces', 'vpns', 'updated_at', 'url')
