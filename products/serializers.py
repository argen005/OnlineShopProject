# serializers.py


from rest_framework import serializers
from .models import Products, Order, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer(many=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields =  ('user', 'product', 'total_cost','adress') 
    def get_total_cost(self, obj):
        total_cost = sum(product.price for product in obj.product.all())
        return total_cost
    
class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()
    
    class Meta:
        model = Review
        fields = ('product', 'user', 'text', 'date')
        