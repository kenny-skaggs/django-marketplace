from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.edit import FormView


class AuthFormViewMixin:
    success_url = reverse_lazy('home')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_login'] = True
        return context

class LoginView(AuthFormViewMixin, FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class RegisterView(AuthFormViewMixin, FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
    
class LogoutView(RedirectView):
    pattern_name = 'home'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
