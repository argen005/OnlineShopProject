from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name    


class Products(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    product = models.ManyToManyField(Products, related_name='orders')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    adress = models.CharField(max_length=50)
    def __str__(self):
        return str(self.user)   

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.product)
    