from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Customers(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(default="Capture.PNG", null=True, blank=True)      # from pillow
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name     # returning the name in admin login in django showing us the name of entry in customers table

class Tag(models.Model):
    name = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),('Outdoor', 'Outdoor'))     # we have ceated categoy as dropdown type wherre we can select random value
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)  # we are using that Category value Here
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (('Pending', 'Pending'),('Out for Delivery','Out for Delivery'),('Delivered', 'Delivered')) # we are creating status value here
    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)  # we are using the status value here
    note = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.product.name


