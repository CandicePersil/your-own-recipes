from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from your_own_recipes import models as recipes_models
from your_own_recipes import serializers as recipes_serializers
# Create your views here.


class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products_list.html"

    def get(self, request, format=None):
        products = recipes_models.Product.objects.all()
        serializer = recipes_serializers.ProductSerializer(
            products,
            many=True
        )
        return Response({"products": serializer.data})


class ProductEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products_edit.html"

    def get(self, request):
        serializer = recipes_serializers.ProductSerializer()
        return Response(
            {
                "serializer": serializer,
                "created": False,
            }
        )

    def post(self, request):
        serializer = recipes_serializers.ProductSerializer(
            data=request.data
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
