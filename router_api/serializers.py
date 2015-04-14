from rest_framework import serializers

from .models import *

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ('time', 'utilization')


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ('time', 'utilization')
        

class VpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vpn


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface


class RouterSerializer(serializers.HyperlinkedModelSerializer):
    cpu = CpuSerializer(many = True, read_only = True)
    memory = MemorySerializer(many = True, read_only = True)
    interfaces = InterfaceSerializer(many = True, read_only = True) 
    vpns = VpnSerializer(many = True, read_only = True)

    class Meta:
        model = Router
        fields = ('name', 'cpu', 'memory', 'interfaces', 'vpns', 'updated_at', 'url')
