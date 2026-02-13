from django.shortcuts import render

from .models import Deployment  
# Create your views here.
def home(request):
    deployments = Deployment.objects.all()

    context = {
        'deployments': deployments
    }   

    return render(request, 'deploy/index.html', context )