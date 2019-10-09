from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models


def home(request):
    categories = models.Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
    
def browse(request, category):
    categories = models.Category.objects.all()
    return render(request, 'browse.html', {'categories': categories})

def login(request):
    message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            message = "Username or password not found."
    
    return render(request, 'login.html', {
        'message': message,
        'hide_login': True
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {
        'form': form,
        'hide_login': True
    })
