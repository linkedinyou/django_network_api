from django.core.management.base import BaseCommand, CommandError
from router_api.models import Router, Vpn

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
            vpn_list = self.gatherVpnData(router.name)
            self.updateRouterVpns(router, vpn_list)


    def gatherVpnData(self, device):
        ''' Add a device vendor check here, for now just use Juniper '''
        device = Juniper(device)
        return device.vpns


    def updateRouterVpns(self, router, vpn_list):
        for vpn in vpn_list:
            new_vpn, created = Vpn.objects.get_or_create(
                router=router,
                name=vpn
                )
            new_vpn.save()
