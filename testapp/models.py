from django.db import models
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('biryani', 'Biryani'),
        ('pizza', 'Pizza'),
        ('noodles', 'Noodles'),
        ('starters', 'Starters'),
        ('dessert', 'Dessert'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.FloatField()
    image_path = models.CharField(max_length=200)