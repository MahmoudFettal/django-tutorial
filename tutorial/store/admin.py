from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sale_start', 'sale_end']

@admin.register(ShoppingCart)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']

@admin.register(ShoppingCartItem)
class ShoppingCartItem(admin.ModelAdmin):
    list_display = ['shopping_cart', 'product', 'quantity']