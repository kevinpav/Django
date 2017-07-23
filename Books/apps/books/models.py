# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=65)
    author = models.CharField(max_length=65)
    published_date = models.DateTimeField()
    category = models.CharField(max_length=16)
    in_print = models.BooleanField(default=True)    # Set default=True so it wouldn't be Null
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)