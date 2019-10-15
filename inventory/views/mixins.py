from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from inventory import models
from . import forms

class AuthFormViewMixin:
    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET['next']
        else:
            return reverse('home')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_login'] = True
        return context

class CategoryDisplayMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context
        
class ItemFormMixin(LoginRequiredMixin, CategoryDisplayMixin):
    login_url = reverse_lazy('login')
    form_class = forms.ItemForm

    def get_success_url(self):
        return reverse('browse', kwargs={'category_name': self.object.category.name})
        
class AuthorCheckMixin:
    def is_user_author_of(self, item):
        if self.request.user.id != item.author_id:
            raise Http404()
        return True
