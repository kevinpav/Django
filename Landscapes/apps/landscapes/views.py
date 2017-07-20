# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Advanced version would use API with dynamic search for Prime# random images, etc.
IMG_SNOW    = "http://i437.photobucket.com/albums/qq99/anhtuan_0510/Winter14.jpg"
IMG_DESERT  = "http://i1374.photobucket.com/albums/ag427/Sharrindra/Pictures/DesertLandscape_1.jpg"
IMG_FOREST  = "http://i177.photobucket.com/albums/w208/layla818/Forest.jpg"
IMG_VINEYARD= "http://i32.photobucket.com/albums/d23/srquinn00/Tahoe11.jpg"
IMG_TROPICAL= "http://img.photobucket.com/albums/v237/Bloody_kisses_13/Myspace%20stuff/tropical-rainforest.jpg"
IMG_NONE    = ""

# Create your views here.
def index(req, route):
    # print("Route: {}".format(route))
    if route is None:
        req.session['image'] = IMG_NONE
    else:
        route = int(route)
        if route > 50 or route < 1:
            req.session['image'] = IMG_NONE
        elif route > 40:
            req.session['image'] = IMG_TROPICAL
        elif route > 30:
            req.session['image'] = IMG_VINEYARD
        elif route > 20:
            req.session['image'] = IMG_FOREST
        elif route > 10:
            req.session['image'] = IMG_DESERT
        else:
            req.session['image'] = IMG_SNOW
    # print("Image= {}".format(req.session['image']))

    return render(req, 'index.html')
