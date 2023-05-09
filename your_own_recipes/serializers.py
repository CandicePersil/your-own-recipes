from rest_framework import serializers
from your_own_recipes import models as recipes_models


class ProductSerializer(serializers.ModelSerializer):

    label = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(
        choices = recipes_models.ProductType.choices
    )

    class Meta:
        model = recipes_models.Product
        fields = ("label", "type")
