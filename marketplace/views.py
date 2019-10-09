from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))