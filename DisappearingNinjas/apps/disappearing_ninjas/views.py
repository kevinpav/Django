# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

ALL_COLORS = ['blue','orange','red','purple']

# Create your views here.
def index(req):

    return render(req, 'index.html')

def ninja(req, route):
    # Initialize or set the session.colors to []
    req.session['colors'] = []
    # If the route is empty, set to ALL_COLORS
    if route == None:
        req.session['colors'] = ALL_COLORS
    # Check if the route is in the known color list
    elif route.lower() in ALL_COLORS:
        req.session['colors'].append(route.lower())
    # If not, show the redhead
    else:
        req.session['colors'].append("other")

    return render(req, 'ninja.html')