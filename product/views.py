
from django.shortcuts import render
from django import forms
from .models import Product, Category, ProductAttribute
from django.db.models import Q
import django_filters
from django_filters import widgets


def colors_list():
    colors = set(ProductAttribute.objects.all().values_list('color', flat=True))
    return list(zip(colors, colors))

def materials_list():
    material = set(ProductAttribute.objects.all().values_list('material', flat=True))
    return list(zip(material, material))

class ProductFilters(django_filters.FilterSet):
    price = django_filters.RangeFilter(label="Price", widget=widgets.RangeWidget(attrs={'placeholder': '100', 'class': 'form-control-sm', 'style':"width:100px"}))
    productattribute__color = django_filters.MultipleChoiceFilter(label="Color", choices=colors_list(), widget=forms.CheckboxSelectMultiple)
    productattribute__material = django_filters.MultipleChoiceFilter(label="Material", choices=materials_list(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Product
        fields = ['price',]

# Create your views here.
def index(request, category_id=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if category_id:
        products=Product.objects.filter(Q(category__id=category_id) | Q(category__parent__id=category_id))
    product_filter = ProductFilters(request.GET, Product.objects.all())
    print(product_filter.qs)
    return render(request, "index.html", {'products': products, 'categories': categories, 'product_filter': product_filter})

def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, 'product_detail.html', {'product':product})