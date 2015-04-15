from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import *

from rest_framework import routers

from router_api.views import *

''' Routers provide an easy way of automatically determining the URL
    configuration.
    
    Here we are registering our 'routers' API from the vpnMonitor app.
    '''
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/devices', RouterViewSet)
router.register(r'api/vpns', VpnViewSet)
router.register(r'api/cpus', CpuViewSet)
router.register(r'api/memorys', MemoryViewSet)
router.register(r'api/routecount', RouteCountViewSet)

urlpatterns = [
    # Include our router URLs from above
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
