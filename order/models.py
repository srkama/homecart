from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class OrderManager(models.Manager):

    def create_order(self, cart, user=None):
        order = self.model.objects.create()
        order.user = user
        order.save()
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, qty=item.qty, price=item.price)
        return order

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    shipping_address = models.TextField(null=True)
    delivery_address = models.TextField(null=True)

    objects = OrderManager()

    def total_price(self):
        return sum([item.total_price() for item in self.items.all()])
    
    def total_items(self):
        return sum([item.qty for item in self.items.all()])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def total_price(self):
        return self.qty * self.price