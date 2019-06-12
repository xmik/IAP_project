from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('branch_offices.urls')),
    path('', include('employees.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]