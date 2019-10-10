from django.http import HttpResponseForbidden
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from inventory import models
from inventory import serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
            
    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return HttpResponseForbidden()
            
    def _update_helper(self, request, partial):
        instance = self.get_object()
        
        if instance.author_id == request.user.id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()
            
    def update(self, request, *args, **kwargs):
        return self._update_helper(request, False);
        
    def partial_update(self, request, *args, **kwargs):
        return self._update_helper(request, True);
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.author_id == request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied()
