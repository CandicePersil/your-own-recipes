from django.urls import path
from your_own_recipes import views


urlpatterns = [
    path('', views.ProductViewSet.as_view({'get': 'list'}), name="products-list"),
    path('add', views.ProductAdd.as_view(), name="products-add"),
    path('delete/<str:id>/', views.delete_product, name="product-delete"),
    path('update/<str:id>/', views.ProductAdd.put, name="product-update"),
    path('details/<pk>/', views.ProductUpdateView.as_view(), name="product"),
    path('types', views.ProductTypesViewSet.as_view({'get': 'list'}), name="products-types"),
    path('types/<str:type>/', views.ProductViewSet.as_view({'get': 'retrieve'}), name="products-by-types")
]