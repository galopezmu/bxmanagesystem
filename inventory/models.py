from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, unique=True, max_length=20)
    description = models.CharField(null=False, unique=True, max_length=250)
    price = models.PositiveIntegerField(null=False)
    state = models.BooleanField(default=True)
    qty = models.PositiveIntegerField(default=0, null=False)
    photo = models.CharField(blank=True, max_length=250)
