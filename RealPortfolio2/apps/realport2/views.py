# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'realport2/index.html')

def projects(req):
    return render(req, 'realport2/projects.html')

def about(req):
    return render(req, 'realport2/about.html')

def testimonials(req):
    return render(req, 'realport2/testimonials.html')