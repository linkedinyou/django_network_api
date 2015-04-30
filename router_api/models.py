from datetime import datetime, timedelta
from django.db.models import *

class Router(Model):
    name = CharField(max_length=200)
    updated_at = DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

class Vpn(Model):
    router = ForeignKey(Router, related_name='vpns')
    name = CharField(max_length=200)
    import_target = CharField(max_length=52)
    route_target = CharField(max_length=52)
    def __str__(self):
        return self.name

class RouteCount(Model):
    vpn = ForeignKey(Vpn, related_name='num_routes')
    time = DateTimeField(default=datetime.now())
    count = IntegerField(default=0)
    def __str__(self):
        return "%s:%s - %s" % (self.vpn, self.time, self.count)

class Interface(Model):
    router = ForeignKey(Router, related_name='interfaces')
    name = CharField(max_length=52)
    description = CharField(max_length=200)
    input_bytes = IntegerField(default=0)
    output_bytes = IntegerField(default=0)
    discards = IntegerField(default=0)
    errors = IntegerField(default=0)
    def __str__(self):
        return self.name

class Cpu(Model):
    router = ForeignKey(Router, related_name='cpus')
    time = DateTimeField()
    utilization = IntegerField(default=0)
    def __str__(self):
        return "%s:%s - %s" % (self.router, self.time, self.utilization)

class Memory(Model):
    router = ForeignKey(Router, related_name='memorys')
    time = DateTimeField()
    utilization = IntegerField(default=0)
    def __str__(self):
        return "%s:%s - %s" % (self.router, self.time, self.utilization)


