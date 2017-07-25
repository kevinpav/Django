# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=65)
#     description = models.CharField(max_length=100)
#     book_id = models.ManyToManyField("Book")
#     category_id = models.ManyToManyField("Category")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=65)
    author = models.CharField(max_length=65) # Normalized to Authors table
    # author_id = models.ManyToManyField("Author") # Changed to ManyToMany for Anthologies assignment
    # published_date = models.DateTimeField()
    category = models.CharField(max_length=16) # Normalized to Category
    # category_id = models.ManyToManyField("Category")
    in_print = models.BooleanField(default=True)    # Set default=True so it wouldn't be Null
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# class Category(models.Model):
#     name = models.CharField(max_length=16)
#     book_id = models.ManyToManyField("Book")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
