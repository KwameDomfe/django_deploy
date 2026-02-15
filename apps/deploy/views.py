from django.shortcuts import render

from .models import Deployment  
# Create your views here.
def home(request):
    deployments = Deployment.objects.all()

    context = {
        'deployments': deployments
    }   

    return render(request, 'deploy/index.html', context )

def deployment_detail(request, deployment_id):
    deployment = Deployment.objects.get(id=deployment_id)

    context = {
        'deployment': deployment
    }

    return render(request, 'deploy/deployment_detail.html', context)