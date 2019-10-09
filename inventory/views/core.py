from django.http import HttpResponse
from django.shortcuts import redirect, render

from inventory import models


def home(request):
    category = models.Category.objects.first()
    return redirect('browse', category=category.name)
    
def browse(request, category):
    categories = models.Category.objects.all()
    return render(request, 'browse.html', {'categories': categories})
