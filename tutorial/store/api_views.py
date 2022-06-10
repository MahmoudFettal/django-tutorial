from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('id',)

class ShoppingCartList(ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    filter_fields = ('id',)
    
    
class ProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    
    def create(self, request, *args,**kwargs):
        return super().create(request, *args,**kwargs)