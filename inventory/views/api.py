from django.http import HttpResponseForbidden
from rest_framework import permissions, status, viewsets
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
            
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
