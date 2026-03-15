from django.urls import path
from . import views

app_name = 'deploy'

urlpatterns = [
    path(
        '', 
        views.deployment_home, 
        name='home'
    ),
    path(
        'create/', 
        views.deployment_create, 
        name='deployment_create'
    ),
    path(
        '<slug:d_slug>/', 
        views.deployment_detail, 
        name='deployment_detail'
    ),
    path(
        '<slug:d_slug>/edit/', 
        views.deployment_update, 
        name='deployment_update'
    ),
    path(
        '<slug:d_slug>/delete/', 
        views.deployment_delete, 
        name='deployment_delete'
    ),
]