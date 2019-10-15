from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from inventory import models
from . import mixins


class HomeView(RedirectView):
    pattern_name = 'browse'
    
    def get_redirect_url(self, *args, **kwargs):
        category = models.Category.objects.first()
        kwargs['category_name'] = category.name
        return super().get_redirect_url(*args, **kwargs)

class BrowseView(mixins.CategoryDisplayMixin, ListView):
    template_name = 'browse.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return models.Item.objects.filter(category__name=self.kwargs['category_name'])
        
class NewItemView(mixins.ItemFormMixin, CreateView):
    template_name = 'item_new.html'
    
    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)
        
class EditItemView(mixins.AuthorCheckMixin, mixins.ItemFormMixin, UpdateView):
    template_name = 'item_edit.html'
    model = models.Item
    
    def get_object(self, *args, **kwargs):
        item = super().get_object(*args, **kwargs)
        if self.is_user_author_of(item):
            return item
            
class ItemDeleteView(mixins.AuthorCheckMixin, RedirectView):
    pattern_name = 'browse'
    
    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(models.Item, id=self.kwargs['item_id'])
        if self.is_user_author_of(item):
            item.delete()
            
            kwargs['category_name'] = item.category.name
            del kwargs['item_id']
            return super().get_redirect_url(*args, **kwargs)
