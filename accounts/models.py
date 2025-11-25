from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CUSTOMER = 'Customer'
    SELLER = 'Seller'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller')
        ]
    
    role = models.CharField(max_length=10,choices= ROLE_CHOICES, default=CUSTOMER)
 
    is_approved = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def save(self,*args, **kwargs):
        if self.role == self.SELLER and self.is_approved == False:
            self.is_approved = False
        super().save(*args, **kwargs) 

    def can_Login(self):
        if self.is_blocked:
            return False 
        if self.role == self.SELLER and not self.is_approved :
            return False
        return True
    
    def __str__(self):
        return f"{self.username} ({self.role})"


