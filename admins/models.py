from django.db import models

from admins.choises import CHOICES


class Prodcuts(models.Model):
    product_name = models.CharField(max_length=200,choices=CHOICES)
    version_name = models.CharField(max_length=200)
    vendor_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    featuers = models.CharField(max_length=200)
    images = models.FileField()