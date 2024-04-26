from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Adjust the max_length as needed
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    password = models.CharField(max_length=255)  # Adjust the max_length as needed
    email = models.EmailField()


class Product(models.Model):
    productName = models.CharField(max_length=255)
    productPrice = models.IntegerField()
    productImage = models.ImageField(default='Image not Found ',blank = True)
    productDescription = models.TextField()
    highestbid = models.IntegerField(default = 0)
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    feedback = models.TextField()
