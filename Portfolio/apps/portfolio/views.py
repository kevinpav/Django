# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'portfolio/index.html')

def testimonials(req):
    return render(req, 'portfolio/testimonials.html')