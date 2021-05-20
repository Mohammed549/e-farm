from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


from base.models import Product, AnimalProduct, FarmProduct
from base.serializer import (
    ProductSerializer,
    AnimalProductSerializer,
    FarmProductSerializer,
)


from rest_framework import status


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductHighestPoints(request):
    queryset = Product.objects.all().order_by("-productPoint")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductHighestPrice(request):
    queryset = Product.objects.all().order_by("-unitPrice")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductLowestPrice(request):
    queryset = Product.objects.all().order_by("unitPrice")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductWithPoints4_5AndHigher(request):

    queryset = Product.objects.filter(productPoint__gte=4.5).order_by("-numReviews")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductWithPoints4(request):
    queryset = Product.objects.filter(productPoint__gte=4.0).order_by("-numReviews")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductWithPoints3_5AndHigher(request):
    queryset = Product.objects.filter(productPoint__gte=3.5).order_by("-numReviews")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFilteredProductWithPoints3(request):
    queryset = Product.objects.filter(productPoint__gte=3).order_by("-numReviews")
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getFarmProducts(request):
    queryset = FarmProduct.objects.all()
    serializer = FarmProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAnimalProducts(request):
    queryset = AnimalProduct.objects.all()
    serializer = AnimalProductSerializer(queryset, many=True)
    return Response(serializer.data)
