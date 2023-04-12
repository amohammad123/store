from store.models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    if validated_data['price'] >= 1000:
      product = Product.objects.create(**validated_data)
      print('product: ', product)
      return product
    else:
      raise serializers.ValidationError("price kamtar az 1000 toman ast")

  class Meta:
    model = Product
    fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartProduct
    fields = ['id', 'price', 'quantity', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
  # cart_products = serializers.SerializerMethodField()

  def create(self, validated_data):
    cart = Cart.objects.filter(user_id=validated_data['user']).last()
    if not cart or cart.checkout:
      cart = Cart.objects.create(**validated_data)

    return {'id':cart.pk, 'user':cart.user, 'checkout': cart.checkout}
  
  class Meta:
    model = Cart
    fields = ['id', 'user', 'checkout']

  # def get_cart_products(self, cart):
  #   cart_products = CartProduct.objects.filter(cart_id=cart.id)
  #   return CartProductSerializer(cart_products).data if cart_products is not None else None


class OrderSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order
    fields = '__all__'