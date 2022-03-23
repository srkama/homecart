from django.db import models

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveIntegerField(default=0)
    comment = models.TextField()