from django.contrib import admin
from .models import Category, Product, ProductAttribute
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'sku_code', 'category', 'price', 'display_image', 'manufacturer')
    list_display = ('name', 'sku_code', 'category', 'price')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)