import random
from django.shortcuts import render
from store.models import *
from store.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
# from django.db.models import Sum

class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

class CartListCreate(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = (IsAuthenticated,)
     
    def filter_queryset(self, queryset):
        queryset = queryset.filter(user_id=1)
        return super().filter_queryset(queryset)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cart_id = response.data.get('id')
        cart_item = request.data['item']
        try:
            product = Product.objects.get(id=cart_item['product_id'])
            # add itme to CartProduct table
            CartProduct.objects.create(cart_id=cart_id,product_id=product.id, price=product.price, quantity=cart_item['quantity'])
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

        return response

class CartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        cart = super().patch(request, *args, **kwargs)
        if cart.data.get('checkout'):
            return Response({'error':'this shopping cart has been paid'}, status=status.HTTP_400_BAD_REQUEST)

        cart_product = get_object_or_404(CartProduct, id=request.data['itme_id'],cart_id=kwargs['id'])
        if 'increment' in request.data:
            cart_product.quantity += 1
            cart_product.save()
        elif 'decrement' in request.data:
            cart_product.quantity -= 1
            cart_product.save()
        return cart

    def delete(self, request, *args, **kwargs):
        cart_product = get_object_or_404(CartProduct, id=request.data['itme_id'],cart_id=kwargs['id'])
        print('cart_product: ', cart_product)
        cart_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


