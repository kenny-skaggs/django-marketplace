from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import RedirectView
from django.views.generic.edit import FormView


    

def login(request):
    message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            message = "Username or password not found."
    
    return render(request, 'login.html', {
        'message': message,
        'hide_login': True
    })

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        auth_login(self.request, user)
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('home')
        
    #TODO: make this a mixin
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_login'] = True
        return context
    
    
class LogoutView(RedirectView):
    pattern_name = 'home'
    
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
