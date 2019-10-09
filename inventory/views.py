from django.http import HttpResponse
from django.shortcuts import render

from . import models


def home(request):
    categories = models.Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
    
def browse(request, category):
    categories = models.Category.objects.all()
    return render(request, 'browse.html', {'categories': categories})

def login(request):
    return render(request, 'login.html', {'hide_login': True})

def register(request):
    return render(request, 'register.html', {'hide_login': True})
