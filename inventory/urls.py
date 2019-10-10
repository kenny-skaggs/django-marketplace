from django.urls import path

from . import views

urlpatterns = [
    path('', views.core.home, name='home'),
    path('browse/<str:category_name>', views.core.browse, name='browse'),
    path('item/new', views.core.item_new, name='item_new'),
    path('item/edit/<int:item_id>', views.core.item_edit, name='item_edit'),
    path('login', views.auth.login, name='login'),
    path('logout', views.auth.logout, name='logout'),
    path('register', views.auth.register, name='register')
]
