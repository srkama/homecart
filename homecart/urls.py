"""homecart URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product import urls as product_urls
from user import urls as user_urls
from cart import urls as cart_urls
from order import urls as order_urls
from review import urls as review_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(product_urls)),
    path('', include(user_urls)),
    path('', include(cart_urls)),
    path('', include(order_urls)),
    path('', include(review_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)