# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def message(req):
    print("Hello from message()")
    return ("Hello")
