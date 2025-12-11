from django.db import models
from django.conf import settings
from products.models import Product
from accounts.models import CustomUser


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled')
    ]

    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='orders'
        )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
        )
    
    address = models.TextField(max_length=100,blank=True, null = True)
    phone = models.CharField(max_length=20 , blank=True, null=True)
    message = models.TextField(max_length=100,blank=True, null = True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items' )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def get_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"    


