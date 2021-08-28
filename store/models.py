from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)

#
#    def __str__(self):
#        return f"{self.user}"


class Product(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    bookname = models.CharField(max_length=100, null=True)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='static/images')
    uploadid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.owner)
        #return self.bookname


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:

            url = ""
        return url


class ShippingAddress(models.Model):
    customer = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.customer)
        #return self.bookname



