# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
# from .models import Book, Author, Category
from .models import Book  # Simplified to one table

# Create your views here.
def index(req):
    context = {
        "books": Book.objects.all()
    }
    return render(req, 'index.html', context)


def addbook(req):
    Book.objects.create(title=req.POST['title'],author=req.POST['author'],category=req.POST['category'])

    return redirect('/')