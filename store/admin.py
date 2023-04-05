from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name','product_price','images','slug')
    list_filter = ('product_price',)
    search_fields = ('product_name','description')
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)






# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ('product_name',)
#     list_editable = ('product_name',)
#     list_display_links = ('product_name',)
#     search_fields = ('image',)
#     prepopulated_fields = {'url':('product_name',)}
#     # raw_id_fields = ('product_price',)
#     # date_hierarchy = 'publish'
#     ordering = ('product_price','product_name')
#

