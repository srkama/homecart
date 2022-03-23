from django.urls import path, include
from rest_framework import routers
from .views import index, product_detail
from .api import CategoryViewset

router = routers.DefaultRouter()
router.register('categories', CategoryViewset)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
    path('<int:category_id>', index, name="category-page"),
    path('<str:product_slug>', product_detail, name="product-page"),
]
