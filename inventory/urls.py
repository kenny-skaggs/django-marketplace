from django.urls import path

from . import views

urlpatterns = [
    path('', views.core.home, name='home'),
    path('browse/<str:category>', views.core.browse, name='browse'),
    path('post', views.core.item, name='item'),
    path('login', views.auth.login, name='login'),
    path('logout', views.auth.logout, name='logout'),
    path('register', views.auth.register, name='register')
]
