from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("Hello, World!")

def me(request):
    return HttpResponse("Hello, World!")

def newHome(request):
    return render(request, 'website/index.html')