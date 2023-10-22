from django.contrib import admin
from .models import Product, Costumer, Cart
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'brand', 'description', 'image', 'catagory']


@admin.register(Costumer)
class Costumer(admin.ModelAdmin):
    list_display = ['id', 'user','name', 'father_name','city', 'locality']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']





# Register your models here.
