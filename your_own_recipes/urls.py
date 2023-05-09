from django.urls import path
from your_own_recipes import views


urlpatterns = [
    path('', views.ProductList.as_view(), name="products-list"),
    path('edit', views.ProductEdit.as_view(), name="products-edit")
]