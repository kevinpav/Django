# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField(max_length=500)
    # description = models.OneToOneField("Description", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# class Description(models.Model):
#     description = models.TextField(max_length=500)
#     # course = models.OneToOneField("Course", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class Book(models.Model):
#     title = models.CharField(max_length=65)
#     author = models.CharField(max_length=65) # Normalized to Authors table
#     # author_id = models.ManyToManyField("Author") # Changed to ManyToMany for Anthologies assignment
#     # published_date = models.DateTimeField()
#     category = models.CharField(max_length=16) # Normalized to Category
#     # category_id = models.ManyToManyField("Category")
#     in_print = models.BooleanField(default=True)    # Set default=True so it wouldn't be Null
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class Category(models.Model):
#     name = models.CharField(max_length=16)
#     book_id = models.ManyToManyField("Book")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
