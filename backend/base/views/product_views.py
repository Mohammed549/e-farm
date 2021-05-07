from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


from base.models import Product, Review
from base.serializer import (
    ProductSerializer
   
    
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

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        description='Deneme',
        unit='Sample Unit',
        countInStock=0,
        category='Sample Category',
        unitPrice=0,

        isFarmProduct=True,
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data['name']
    product.description = data['description']
    product.unit = data['unit']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.unitPrice = data['unitPrice']
    product.isFarmProduct = data['isFarmProduct']
    

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()

    return Response('Producted Deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 2 - No Rating or 0
    elif data['productPoint'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            productPoint=data['productPoint'],
            deliveryPoint=data['deliveryPoint'],
            comment=data['comment'],
        )

        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.productPoint

        product.productPoint = total / len(reviews)
        product.save()

        #4- Go User find all product rating and update farmerPoint

        return Response('Review Added')



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







