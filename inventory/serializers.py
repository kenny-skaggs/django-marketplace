from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(many=False)
    class Meta:
        model = models.Item
        fields = '__all__'
