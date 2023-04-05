from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# todo custom user for extera data and login control
# Create your models here.
class ProductBrand(models.Model):
    brand_name=models.CharField(max_length=250)

# class Attributes(models.Model):
#     pass

class Product(models.Model):
    product_code=models.IntegerField(unique=True)
    product_name=models.CharField(max_length=250)
    images=models.ImageField(upload_to='store/p')
    product_price=models.IntegerField()
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    created_time=models.DateTimeField(default=timezone.now)
    updated_time=models.DateTimeField(auto_now=True)
    product_brand=models.ForeignKey(ProductBrand,on_delete=models.PROTECT)
    # Attributes=models.ForeignKey(Attributes)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)

    def total_price(self):
        total=0
        for cart_item in self.cartitems.all():
            total +=(cart_item.price * cart_item.quantity)
            return int(total)
    def __str__(self):
        return self.User.username

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cartitems')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    quantity=models.PositiveSmallIntegerField()

    def total_price(self):
        return int(self.price * self.quantity)

    def __str__(self):
        return self.product.product_name

class payment(models.Model):
    pass





    # brand=models.ForeignKey.many_to_one(ProductBrand,)
    # buy_price=models.FloatField()
    # sell_price=models.FloatField()

    # order_date=models.DateTimeField(auto_now_add=True)
# class Customer(models.Model):
#     first_name=models.CharField(max_length=250)
#     last_name=models.CharField(max_length=250)
#     Email=models.CharField(max_length=250)
#     tel=models.IntegerField()
#     address=models.TextField()












