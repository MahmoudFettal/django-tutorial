from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

# Product views:
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    
class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('id',)
    
class ProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

# Product views:
class ShoppingCartCreateView(CreateAPIView):
    serializer_class = ShoppingCartSerializer
    
class ShoppingCartList(ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    filter_fields = ('id',)

class ShoppingCartView(RetrieveUpdateDestroyAPIView):
    queryset =  ShoppingCart.objects.all()
    lookup_field = 'id'
    serializer_class = ShoppingCartSerializer

# Product views:
class ShoppingCartItemCreateView(CreateAPIView):
    serializer_class = ShoppingCartItemSerializer

class ShoppingCartItemsList(ListAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer
    filter_fields = ('id',)
    
class ShoppingCartItemView(RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCartItem.objects.all()
    lookup_field = 'id'
    serializer_class = ShoppingCartItemSerializer