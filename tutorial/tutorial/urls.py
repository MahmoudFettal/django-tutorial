"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.api_views import *

urlpatterns = [
    # products APIs
    path('api/products/', ProductsList.as_view()),
    path('api/products/create', ProductCreateView.as_view()),
    path('api/products/<int:id>', ProductView.as_view()),
    # products APIs
    path('api/shoppingcarts/', ShoppingCartList.as_view()),
    path('api/shoppingcarts/create', ShoppingCartCreateView.as_view()),
    path('api/shoppingcarts/<int:id>', ShoppingCartView.as_view()),
    # products APIs
    path('api/shoppingcartitems/', ShoppingCartItemsList.as_view()),
    path('api/shoppingcartitems/create', ShoppingCartItemCreateView.as_view()),
    path('api/shoppingcartitems/<int:id>', ShoppingCartItemView.as_view()),
    path('admin/', admin.site.urls),
]
