from django.db import models


class Category(models.Model):
    name = models.TextField()

class Item(models.Model):
    title = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, related_name="items", null=False, on_delete=models.CASCADE)
