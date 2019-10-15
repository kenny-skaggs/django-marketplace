from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name;

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, related_name="items", null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
