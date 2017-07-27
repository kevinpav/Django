# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

MINLENGTH = 2
MAXLENGTH = 25
MINPASS = 9

def validateLength(arg):
    if len(arg) < MINLENGTH:
        raise ValidationError(
            "{} must be longer than {}".format(arg, MINLENGTH)
        )
    elif len(arg) > MAXLENGTH:
        raise ValidationError(
            "{} must be shorter than {}".format(arg, MINLENGTH)
        )

def validatePasswd(arg):
    if len(arg) < MINPASS:
        raise ValidationError(
            "Password must be longer than {}".format(MINPASS)
        )

def validateEmail(arg):
    pass


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25,
            validators=[validateLength])
    last_name = models.CharField(max_length=25,
            validators=[validateLength])
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25,
            validators=[validatePasswd])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = UserManager()
    
    def __str__(self):
        return self.email

# class FunUser(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
