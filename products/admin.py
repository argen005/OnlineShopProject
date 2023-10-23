from django.contrib import admin

# Register your models here.

from .models import Products, Order, Category, Review
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Review)