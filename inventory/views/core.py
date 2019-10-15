from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView
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
        
class NewItemView(CategoryDisplayMixin, CreateView):
    form_class = forms.ItemForm
    template_name = 'item_new.html'
    
    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return redirect('browse', self.object.category.name)
    
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
