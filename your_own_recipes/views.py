from django.forms import formset_factory
from django.http import Http404
from django.shortcuts import get_list_or_404
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status, viewsets
from your_own_recipes import forms as recipes_forms
from your_own_recipes import models as recipes_models
from your_own_recipes import serializers as recipes_serializers
# Create your views here.


class ProductView(TemplateView):
    template_name = "product_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = recipes_models.Product.objects.get(id=context["id"])
        return context


class ProductViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    form_class = recipes_forms.ProductForm
    template_name = "products_list.html"

    def list(self, request):
        products = recipes_models.Product.objects.all()
        serializer = recipes_serializers.ProductSerializer(
            products,
            many=True
        )
        return Response({"products": serializer.data})


    def retrieve(self, request, type=None, pk=None):
        queryset = recipes_models.Product.objects.all()
        products = get_list_or_404(queryset, type=type)
        serializer = recipes_serializers.ProductSerializer(
            products,
            many=True
        )
        return Response({"type": type, "products": serializer.data})


class ProductAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products_add.html"

    def get(self, request):
        serializer = recipes_serializers.ProductSerializer()
        return Response(
            {
                "serializer": serializer,
                "created": False,
            }
        )

    def put(self, request, id):
        try:
            product = recipes_models.Product.objects.get(id=id)
        except recipes_models.Product.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        serializer = recipes_serializers.ProductSerializer(
            product,
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        serializer = recipes_serializers.ProductSerializer(
            data=data
        )
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                        "serializer": serializer,
                        "created": True,
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as err:
                return Response({
                        "serializer": serializer,
                        "created": False,
                        "error": str(err),
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response({
                "serializer": serializer,
                "created": False,
                "error": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


def delete_product(request, **kwargs):
    product = get_object_or_404(
        recipes_models.Product,
        id=kwargs["id"],
    )
    if product:
        product.delete()
        return redirect("products-list")


class ProductTypesViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products_types_list.html"

    def list(self, request):
        types = recipes_models.ProductType
        return Response({"types": types})