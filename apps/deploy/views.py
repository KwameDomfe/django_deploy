from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.accounts.models import UserProfile
from apps.accounts.permissions import role_required

from .forms import DeploymentForm
from .models import Deployment


# Deployment List Views
@login_required
def deployment_home(request):
    deployments = Deployment.objects.all().order_by('-created_at')

    context = {
        'deployments': deployments
    }

    return render(request, 'deploy/index.html', context)
    
#  Deployment Detail Views
@login_required
def deployment_detail(request, d_slug):

    deployment = get_object_or_404(Deployment, slug=d_slug)
    form = DeploymentForm(instance=deployment)

    context = {
        'deployment': deployment,
        'form': form,
    }

    return render(request, 'deploy/deployment_detail.html', context)

# Deployment Create Views
@login_required
@role_required([UserProfile.Role.ADMIN, UserProfile.Role.EDITOR])
def deployment_create(request):
    if request.method == 'POST':
        form = DeploymentForm(request.POST, request.FILES)
        if form.is_valid():
            deployment = form.save()
            return redirect(deployment)
    else:
        form = DeploymentForm()

    context = {
        'form': form,
        'page_title': 'Create Deployment',
        'submit_label': 'create',
    }
    return render(request, 'deploy/deployment_form.html', context)

# Deployment Update Views
@login_required
@role_required([UserProfile.Role.ADMIN, UserProfile.Role.EDITOR])
def deployment_update(request, d_slug):
    deployment = get_object_or_404(Deployment, slug=d_slug)

    if request.method == 'POST':
        form = DeploymentForm(
            request.POST, 
            request.FILES, 
            instance=deployment
        )
        if form.is_valid():
            updated_deployment = form.save()
            return redirect(updated_deployment)
    else:
        form = DeploymentForm(instance=deployment)

    context = {
        'form': form,
        'deployment': deployment,
        'page_title': 'Edit Deployment',
        'submit_label': 'Save Changes',
    }
    return render(request, 'deploy/deployment_form.html', context)

# Deployment Delete Views
@login_required
@role_required([UserProfile.Role.ADMIN])
def deployment_delete(request, d_slug):
    deployment = get_object_or_404(Deployment, slug=d_slug)

    if request.method == 'POST':
        deployment.delete()
        return redirect('home')

    context = {
        'deployment': deployment,
    }
    return render(request, 'deploy/deployment_confirm_delete.html', context)

