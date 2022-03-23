from rest_framework import serializers
from .models import Category

class CatergorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'