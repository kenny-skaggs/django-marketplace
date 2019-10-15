from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import RedirectView
from django.views.generic.list import ListView

from inventory import models
from . import forms


class HomeView(RedirectView):
    pattern_name = 'browse'
    
    def get_redirect_url(self, *args, **kwargs):
        category = models.Category.objects.first()
        kwargs['category_name'] = category.name
        return super().get_redirect_url(*args, **kwargs)
        
class CategoryDisplayMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context

class BrowseView(CategoryDisplayMixin, ListView):
    template_name = 'browse.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return models.Item.objects.filter(category__name=self.kwargs['category_name'])
    
def item_new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = forms.ItemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.author_id = request.user.id
                item.save()
                
                return redirect('browse', item.category.name)
        else:
            form = forms.ItemForm()
        
        categories = models.Category.objects.all()
        return render(request, 'item_new.html', {
            'categories': categories,
            'form': form
        })
    
def item_edit(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    
    if item.author_id != request.user.id:
        return HttpResponseForbidden()
    else:
        if request.method == "POST":
            form = forms.ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('browse', item.category.name)
        else:
            form = forms.ItemForm(instance=item)
            
        categories = models.Category.objects.all()
        return render(request, 'item_edit.html', {
            'categories': categories,
            'form': form
        })
    
def item_delete(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    
    if item.author_id != request.user.id:
        return HttpResponseForbidden()
    else:
        item.delete()
        return redirect('browse', item.category.name)
