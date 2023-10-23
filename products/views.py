from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics
from .models import Products, Order, Review
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
from .serializers import ReviewSerializer
from django.http import HttpResponse



class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


    def list(self, request, *args, **kwargs):
        print(request.user)
    
        queryset = self.filter_queryset(self.get_queryset())
 
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    
    
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


 # views.py от ЧатаГПТ
class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        print(product_id)
        print(Products.objects.all()[3].id)
        return Review.objects.filter(product__id=product_id)


def delete_products(request):
    Products.objects.all().delete()
    return HttpResponse({'delete': 'done'}, content_type='application/json')
