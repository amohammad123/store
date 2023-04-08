from django.shortcuts import render
from store.models import *
from store.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(ListCreateAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
