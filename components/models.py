from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Component(models.Model):

    CATEGORY_CHOICES = [
        ('CPU', 'CPU'),
        ('GPU', 'GPU'),
        ('RAM', 'RAM'),
        ('SSD', 'SSD'),
        ('PSU', 'Power Supply'),
        ('CASE', 'Case'),
        ('COOLER', 'Cooler'),
        ('MOTHERBOARD', 'Motherboard'),
        ('FAN', 'Fan')
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta: 
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.name} | {self.price}"
