# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

MINLENGTH = 8
MAXLENGTH = 25

def validateLength(arg):
    if len(arg) < MINLENGTH:
        raise ValidationError(
            "{} must be longer than {}".format(arg, MINLENGTH)
        )
    elif len(arg) > MAXLENGTH:
        raise ValidationError(
            "{} must be shorter than {}".format(arg, MINLENGTH)
        )

# Create your models here.
class User(models.Model):
    username = models.CharField(
            max_length=25,
            validators=[validateLength]
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = UserManager()
    
    def __str__(self):
        return self.username

# class FunUser(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
