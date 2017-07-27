# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
import re

MINLENGTH = 2
MAXLENGTH = 25
MINPASS = 9
# Create the regex we will use to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.]')

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
    if not EMAIL_REGEX.match(arg):
        raise ValidationError(
            "Email format is invalid"
        )

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25,
            validators=[validateLength])
    last_name = models.CharField(max_length=25,
            validators=[validateLength])
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25,
            validators=[validatePasswd, validateEmail])
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
