# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=16)
    store_id = models.ManyToManyField("Store")  # Added for Optional assignment
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Store(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    product_id = models.ManyToManyField("Product")  # Added for Optional assignment
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    