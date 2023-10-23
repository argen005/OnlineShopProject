from django.contrib import admin
from django.urls import path, include
from products.views import ProductsViewSet, OrderDetailView, ReviewViewSet
from rest_framework.routers import DefaultRouter
from products.views import delete_products

router = DefaultRouter()
router.register('products', ProductsViewSet)
router.register(r'reviews/(?P<product_id>\d+)', ReviewViewSet, basename='product-reviews')
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  
    path('api/accounts/', include('user.urls')), 
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('delete_products/', delete_products),
] + router.urls


