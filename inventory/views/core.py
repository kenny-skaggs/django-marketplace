from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, UpdateView
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
        
class ItemFormMixin(LoginRequiredMixin, CategoryDisplayMixin):
    login_url = reverse_lazy('login')
    form_class = forms.ItemForm

    def get_success_url(self):
        return reverse('browse', kwargs={'category_name': self.object.category.name})
        
class NewItemView(ItemFormMixin, CreateView):
    template_name = 'item_new.html'
    
    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)
        
class AuthorCheckMixin:
    def is_user_author_of(self, item):
        if self.request.user.id != item.author_id:
            raise Http404()
        return True
        
class EditItemView(AuthorCheckMixin, ItemFormMixin, UpdateView):
    template_name = 'item_edit.html'
    model = models.Item
    
    def get_object(self, *args, **kwargs):
        item = super().get_object(*args, **kwargs)
        if self.is_user_author_of(item):
            return item
            
class ItemDeleteView(AuthorCheckMixin, RedirectView):
    pattern_name = 'browse'
    
    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(models.Item, id=self.kwargs['item_id'])
        if self.is_user_author_of(item):
            item.delete()
            
            kwargs['category_name'] = item.category.name
            del kwargs['item_id']
            return super().get_redirect_url(*args, **kwargs)
