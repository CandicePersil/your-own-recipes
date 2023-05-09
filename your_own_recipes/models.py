from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductType(models.TextChoices):
    VEGETABLES_BEANS = "VEGETABLES_BEANS", _("Vegetables, legumes and beans")
    FRUITS = "FRUITS", _("Fruits")
    GRAINS_CEREALS_NUTS = "GRAINS_CEREALS_NUTS", _("Grains, cereals and nuts")
    MEAT_POULTRY = "MEAT_POULTRY", _("Meat and poultry")
    FISH_SEAFOOD = "FISH_SEAFOOD", _("Fish and seafood")
    DAIRY_FOODS = "DAIRY_FOODS", _("Dairy foods")
    FATS_OILS_SWEETS = "FATS_OIL_SWEETS", _("Fats, oils and sweets")
    SEASONING = "SEASONING", _("Seasoning")
    ALCOHOL = "ALCOHOL", _("Alcohol")


class UnitOfMeasurement(models.TextChoices):
    MILLILITER = "MILLILITER", _("Millimeter")
    GRAM = "GRAM", _("Gram")
    POUND = "POUND", _("Pound")
    TEASPOON = "TEASPOON", _("Teaspon")
    DESSERTSPOON = "DESSERTSPOON", _("Dessertspoon")
    TABLESPOON = "TABLESPOON", _("Tablespoon")
    CUP = "CUP", _("Cup")
    POINT = "POINT", _("Point")
    QUART = "QUART", _("Quart")
    GALLON = "GALLON", _("Gallon")
    UNIT = "UNIT", _("Unit")


class Product(models.Model):
    label = models.CharField(max_length=300)
    type = models.CharField(
        max_length=30,
        choices=ProductType.choices,
        default=ProductType.VEGETABLES_BEANS,
    )

    class Meta:
        unique_together = ("label", "type")


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=None, null=False)
    unit = models.CharField(
        max_length=20,
        choices=UnitOfMeasurement.choices,
        default=UnitOfMeasurement.UNIT,
    )


class Step(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=2000)
    next_step = models.ForeignKey("self", on_delete=models.CASCADE)


class Recipe(models.Model):
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
