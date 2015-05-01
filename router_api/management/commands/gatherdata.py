from django.core.management.base import BaseCommand, CommandError
from router_api.models import Router, Vpn, RouteCount

import netw0rk

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
	    if router.vendor.name == 'juniper':
	    	device = netw0rk.Juniper(router.name)
	    else:
		''' Build a generic device '''
		device = netw0rk.Device(router.name)
            self.updateRouterVpns(router, device.vpns)
            self.updateRouteCounts(router, device)


    def updateRouterVpns(self, router, vpn_list):
        for vpn in vpn_list:
            new_vpn, created = Vpn.objects.get_or_create(
                router=router,
                name=vpn
                )
            new_vpn.save()


    def updateRouteCounts(self, router, device):
        for vpn_count in device.vpn_num_routes:
            vpn_name, route_count = vpn_count
            vpn = Vpn.objects.get(router=router, name=vpn_name)
            RouteCount.objects.create(
                vpn=vpn,
                count=route_count
                )
