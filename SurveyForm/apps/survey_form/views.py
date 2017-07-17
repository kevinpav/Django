# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random, string

# Create your views here.
def index(req):
    # Display index/form
    return render(req, 'index.html')

def process(req):
    # If numtries is not defined, define it
    if 'numtries' not in req.session:
        req.session['numtries'] = 1
    # If POST then set session variables with Form fields
    if req.method == "POST":
        req.session['name'] = req.POST['name']
        req.session['location'] = req.POST['location']
        req.session['language'] = req.POST['language']
        req.session['comment'] = req.POST['comment']
        req.session['numtries'] += 1
    # Redirect to the results page
    return redirect('/result')

def result(req):
    # Display results page
    return render(req, 'result.html')

def reset(req):
    if req.method == "POST":
        # Reset/Delete session variables
        del req.session['name']
        del req.session['location']
        del req.session['language']
        del req.session['comment']
    # Then redirect back to index.html
    return redirect('/')
