from django.db import models
from django.contrib.auth.models import AbstractUser

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name  

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    requirement = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/', blank=True, null=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name



class NewUser(AbstractUser):
    wishlist = models.ManyToManyField('Product', blank=True, related_name='wishlists')

    
    

# Create your models here.
