from xml.etree.ElementInclude import include
from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        exclude = ()

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        exclude = ()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["amount"] = instance.subtotal()
        data["after_tax"] = instance.taxes()
        data["total"] = instance.total()
        data["items"] = instance.cart_items()
        
        return data
