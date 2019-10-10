from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from inventory import models
from . import forms


def home(request):
    category = models.Category.objects.first()
    return redirect('browse', category_name=category.name)
    
def browse(request, category_name):
    categories = models.Category.objects.all()
    items = models.Item.objects.filter(category__name=category_name)
    return render(request, 'browse.html', {
        'categories': categories,
        'items': items
    })
    
def item_new(request):
    if request.method == "POST":
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author_id = request.user.id
            item.save()
            
            return redirect('home')
    else:
        form = forms.ItemForm()
    
    categories = models.Category.objects.all()
    return render(request, 'item.html', {
        'categories': categories,
        'form': form
    })
    
def item_edit(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == "POST":
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('browse', 'Auto')
    else:
        form = forms.ItemForm(instance=item)
        
    
    categories = models.Category.objects.all()
    return render(request, 'item.html', {
        'categories': categories,
        'form': form
    })
