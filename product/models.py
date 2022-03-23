from tabnanny import verbose
from unicodedata import category
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager



# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    @property
    def get_product_count(self):
        return sum([child.products.count() for child in self.children.all()]) + self.products.count()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    sku_code=models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    manufacturer = models.CharField(max_length=100)
    display_image = models.ImageField() 

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.name
            slug = slug.replace(' ', '-')
            if Product.objects.filter(slug=slug):
                slug=slug+'-'+Product.objects.filter(slug=slug).count()
            self.slug=slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def rating(self):
        return self.reviews.all().aggregate(models.Avg('stars'))['stars__avg']

class ProductAttribute(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    material = models.CharField(max_length=20)
    tags = TaggableManager()

    def __str__(self):
        return str(self.product)