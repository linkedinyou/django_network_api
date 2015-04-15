from django.core.management.base import BaseCommand, CommandError
from router_api.models import Router

from netw0rk import Juniper

class Command(BaseCommand):
        help = 'Polls a device for all of the information we need in our router API'

        def handle(self, *args, **options):
            for router in Router.objects.all():
                self.gatherData(router.name)

        def gatherData(self, device):
            device = Juniper(device)
            for vpn in device.vpns:
                print vpn
