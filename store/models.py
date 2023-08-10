from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Running', 'Running'),
        ('Training', 'Training'),
        ('Yoga', 'Yoga'),
        ('Swimming', 'Swimming'),
        ('Cycling', 'Cycling'),
        # Add more categories as needed
    )

    GENDER_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='store/static/images')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
