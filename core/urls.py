from django.contrib import admin
from django.urls import include, path

from .views import (hello_world, health_check)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        '',
        hello_world, 
        name='hello_world'),
    path('health/',
        health_check, 
        name='health_check'),
    path('deploy/',
        include('apps.deploy.urls')),
]
