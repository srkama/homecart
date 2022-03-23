from django.urls import path
from .views import checkout, payment

urlpatterns = [
    path('checkout', checkout),
    path('payment', payment),
]
