from django.core.management.base import BaseCommand, CommandError
from router_api.models import Router

from netw0rk import Juniper

class Command(BaseCommand):
    ''' This management script could be used by cron to schedule 
        gathering data from all of the devices in our database.

        Unfortunately, this is just an example as my "desktop" that I
        am building this on does not have access to the management network to pull
        router data.

        I will have to use the API to write data from a bastion host.
        '''
    help = 'Polls a device for all of the information we need in our router API'

    def handle(self, *args, **options):
        for router in Router.objects.all():
            self.gatherData(router.name)

    def gatherData(self, device):
        device = Juniper(device)
        for vpn in device.vpns:
            print vpn
            ''' Save each VPN into the database for this device, etc. '''

        ''' write out device.cpu, device.memory, etc '''
