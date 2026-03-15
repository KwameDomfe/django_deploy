from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def hello_world(request):
  context = {}
  return render(request, "index.html", context)

@login_required
def health_check(request):
    return HttpResponse("OK")