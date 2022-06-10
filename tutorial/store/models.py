from django.db import models

# Create your models here.

from django.utils import timezone
from django.db import models

class Product(models.Model):
    DISCOUNT_RATE = 0.10

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __str__(self):
        return str(self.id) + "-" +self.name

class ShoppingCart(models.Model):
    TAX_RATE = 0.13
  
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def subtotal(self):
        shoppingCartItems = ShoppingCartItem.objects.filter(shopping_cart_id = self.id)
        amount = 0.0
        for item in shoppingCartItems:
            amount += item.quantity * item.product.price
        return round(amount, 2)

    def cart_items(self):
        shoppingCartItems = ShoppingCartItem.objects.filter(shopping_cart_id = self.id)
        items_list = []

        for item in shoppingCartItems:
            items_list.append(item.product.name)

        return items_list
    
    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() + self.taxes(), 2)
 
    def __str__(self):
        return str(self.id) + "-" +self.name

class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, related_name='items', related_query_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total(self):
        return round(self.quantity * self.product.current_price())

    def __str__(self):
        return str(self.id) + "-Cart -" + str(self.shopping_cart) + "Product -" + str(self.product) + "Product-" + str(self.quantity)
