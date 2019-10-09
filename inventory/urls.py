from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/<str:category>', views.browse, name='browse'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
