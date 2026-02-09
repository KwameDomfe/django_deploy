from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
  context = {}
  return render(request, "hello_world.html", context)

def health_check(request):
    return HttpResponse("OK")