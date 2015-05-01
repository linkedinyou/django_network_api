# django_network_api
Backend API for routers and switches written in Django. Uses the netw0rk framework to gather SNMP data from devices.

Requires Django 1.8+ and some additional Django packages (django-rest-framework, etc.)
I will eventually add a setup.py include to manage dependencies.

# Example gathering data
    ''' Create our default SQLITE3 database '''
    ./manage.py migrate
    
    ''' Add a couple records from the shell, quick and dirty '''
    ./manage.py shell
    from router_api.models import Router, Vendor
    vendor = Vendor(name='juniper')
    vendor.save()
    router = Router(name='some.device', vendor=vendor)
    router.save()
    router.objects.all()
    
    ''' Gather data for the device we just added '''
    ./manage.py gatherdata

# View your data through the API
* ./manage.py runserver 0.0.0.0:8000
* http://your-server:8000
