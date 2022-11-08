from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Hello(request):
    return HttpResponse('Hello World')


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
