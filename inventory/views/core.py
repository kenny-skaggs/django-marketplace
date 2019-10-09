from django.http import HttpResponse
from django.shortcuts import redirect, render

from inventory import models
from . import forms


def home(request):
    category = models.Category.objects.first()
    return redirect('browse', category=category.name)
    
def browse(request, category):
    categories = models.Category.objects.all()
    items = models.Item.objects.filter(category__name=category)
    return render(request, 'browse.html', {
        'categories': categories,
        'items': items
    })
    
def item(request):
    if request.method == "POST":
        form = forms.ItemForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('browse', 'Auto')
    else:
        form = forms.ItemForm()
        
    
    categories = models.Category.objects.all()
    return render(request, 'item.html', {
        'categories': categories,
        'form': form
    })
