from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=(
        (LIVE,'Live'),(DELETE,'Delete'))
    CART_STAE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4

    STATUS_CHOICES=((CART_STAE,'Cart State'), (ORDER_CONFIRMED,'Order Confirmed'), (ORDER_PROCESSED,'Order Processed'), (ORDER_DELIVERED,'Order Delivered'), (ORDER_REJECTED,'Order Rejected'))
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAE)

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts', null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order, on_delete=models.CASCADE,related_name="added_items")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)