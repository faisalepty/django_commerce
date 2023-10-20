from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pic = models.ImageField()

    def __str__(self):
        return self.name   
    
class Oder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def Total(self):
        return self.quantity * self.products.price
