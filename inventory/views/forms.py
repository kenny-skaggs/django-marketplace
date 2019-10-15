from django.forms import ModelChoiceField, ModelForm

from inventory import models


class CategoryModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ItemForm(ModelForm):
    category = CategoryModelChoiceField(queryset=models.Category.objects.all())
    class Meta:
        model = models.Item
        exclude = ['author']
        
    def save(self, user=None):
        item = super().save(commit=False)
        if user:
            item.author_id = user.id
        item.save()
        return item