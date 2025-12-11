from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name
        

class CustomUser(models.Model):
    CUSTOMER = 'Customer'
    SELLER = 'Seller'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller')
        ]
    
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique = True)
    hashed_password = models.CharField(max_length=300)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank =True, null = True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank =True, null = True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=200, blank=True)
    last_login = models.DateTimeField(blank=True,null=True)
    is_approved = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    is_authenticated = models.BooleanField(default=False)


    # @property
    # def is_authenticated(self):
    #     return True
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_active(self):
        return True
    
    def set_password(self, password):

        self.hashed_password = make_password(password)

    def check_password(self,password):

        return check_password(password, self.hashed_password)    

    def get_session_auth_hash(self):
        return self.hashed_password

    
    def __str__(self):
        return f"{self.username} ({self.role})"
    

# class User(AbstractUser):
#     CUSTOMER = 'Customer'
#     SELLER = 'Seller'
#     ROLE_CHOICES = [
#         (CUSTOMER, 'Customer'),
#         (SELLER, 'Seller')
#         ]
    
#     role = models.CharField(max_length=10,choices= ROLE_CHOICES, default=CUSTOMER)
 
#     is_approved = models.BooleanField(default=False)
#     is_blocked = models.BooleanField(default=False)

#     def save(self,*args, **kwargs):
#         if self.role == self.SELLER and self.is_approved == False:
#             self.is_approved = False
#         super().save(*args, **kwargs) 

#     def can_Login(self):
#         if self.is_blocked:
#             return False 
#         if self.role == self.SELLER and not self.is_approved :
#             return False
#         return True
    
#     def __str__(self):
#         return f"{self.username} ({self.role})"


