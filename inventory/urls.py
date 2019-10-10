from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.api.CategoryViewSet)
router.register(r'items', views.api.ItemViewSet)

urlpatterns = [
    path('', views.core.home, name='home'),
    path('browse/<str:category_name>', views.core.browse, name='browse'),
    path('item/new', views.core.item_new, name='item_new'),
    path('item/edit/<int:item_id>', views.core.item_edit, name='item_edit'),
    path('item/delete/<int:item_id>', views.core.item_delete, name='item_delete'),
    path('login', views.auth.login, name='login'),
    path('logout', views.auth.logout, name='logout'),
    path('register', views.auth.register, name='register'),
    path('api/', include(router.urls))
]
