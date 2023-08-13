from django.forms import ModelForm
from your_own_recipes import models as recipes_models


class ProductForm(ModelForm):
    class Meta:
        model = recipes_models.Product
        fields = ["label", "type"]