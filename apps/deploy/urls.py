from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:deployment_id>/', 
        views.deployment_detail, 
        name='deployment_detail'),
]