from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from accounts.models import CustomUser,City

class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )

    name = models.CharField(max_length=100, unique=True)
    available_in = models.ManyToManyField(City,related_name='products', blank = True)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(blank= True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    image = models.ImageField(upload_to='product_image/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)

        if creating and not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}-{self.id}"
            self.save()

    def __str__(self):
        return self.name


