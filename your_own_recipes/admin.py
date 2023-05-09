from django.contrib import admin
from your_own_recipes import models as recipes_models

# Register your models here.
admin.site.register(recipes_models.Product)
admin.site.register(recipes_models.Ingredient)
admin.site.register(recipes_models.Step)
admin.site.register(recipes_models.Recipe)
