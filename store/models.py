from django.db import models
from blog.models import Image
from django.contrib.auth.models import User

# todo custom user for extera data and login control
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'categorys'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    images = models.ImageField(upload_to='store/images')
    price = models.IntegerField()
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name