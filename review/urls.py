from django.urls import path
from .views import product_review

urlpatterns = [
    path('review/<int:product_id>', product_review, name="product-review"),
]
