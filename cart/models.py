from audioop import maxpp
from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class CartManager(models.Manager):

    def get_or_new_cart(self, request):
        cart_id = request.session.get('cart')

        print('cart id found in request', cart_id)
        
        if cart_id:
            try:
                cart = self.model.objects.get(id=cart_id)
                print('cart found', cart)
            except:
                cart = Cart.objects.create()
        else:
            cart = Cart.objects.create()

        request.session['cart']=cart.id
        
        return cart


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    objects = CartManager()

    def __str__(self):
        return 'cart:'+str(self.id)

    def add_product(self, product):
        product = Product.objects.get(id=product)
        cart_items = CartItem.objects.filter(cart=self, product=product)
        if cart_items:
            cart_items[0].qty = cart_items[0].qty+1
            cart_items[0].save()
        else:
            CartItem.objects.create(cart=self, product=product, qty=1, price=product.price)

## Total value of cart
## Sum of products total price (qty * price)

    def total_price(self):
        return sum([item.total_price() for item in self.items.all()])
    
    def total_items(self):
        return sum([item.qty for item in self.items.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def total_price(self):
        return self.qty * self.price