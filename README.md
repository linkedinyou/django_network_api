# django_network_api
Backend API for routers and switches written in Django. Uses the netw0rk framework to gather SNMP data from devices.

# Example gathering data
    ./manage.py migrate
    ./manage.py shell
    from router_api.models import Router, Vendor
    vendor = Vendor(name='juniper')
    vendor.save()
    router = Router(name='some.device', vendor=vendor)
    router.save()
    router.objects.all()
    ./manage.py gatherdata

# View your data through the API
* ./manage.py runserver
* http://your-server:your:port/api/
