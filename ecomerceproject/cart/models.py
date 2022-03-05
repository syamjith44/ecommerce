from django.db import models
from shop.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.title




