# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return render(req, 'index.html')

def create(req):
	if req.method == "POST":
		print "*"*50
		print req.POST
		print req.method
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")