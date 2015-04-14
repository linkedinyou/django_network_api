from django.contrib import admin
from .models import *

admin.site.register(Router)
admin.site.register(Interface)
admin.site.register(Cpu)
admin.site.register(Vpn)
admin.site.register(Memory)

# Register your models here.
