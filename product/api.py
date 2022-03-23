from rest_framework import viewsets
from .models import Category
from .serializers import CatergorySerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CatergorySerializer