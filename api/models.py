from django.db import models

# Create your models here.



class HomeProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    image = models.ImageField(upload_to = 'image', blank=True)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
