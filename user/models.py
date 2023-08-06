from django.db import models

from user.choices import CHOICES
from admins.models import Prodcuts

class Users(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profession=models.CharField(max_length=200,choices=CHOICES)
    email=models.EmailField(max_length=200)
    mobile=models.CharField(max_length=20)
    location=models.CharField(max_length=200)

class Purchase(models.Model):
    customer = models.ForeignKey(Users,on_delete=models.CASCADE)
    purhased = models.ForeignKey(Prodcuts,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalprice = models.FloatField()
    status = models.CharField(max_length=200,default='incart')

class Feedback(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    product=models.ForeignKey(Prodcuts,on_delete=models.CASCADE)
    isPurchased=models.CharField(max_length=200,default='pending')
    rating=models.CharField(max_length=200)
    review=models.CharField(max_length=200)
    sentiment=models.CharField(max_length=200)