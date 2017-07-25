# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
# from .models import Book, Author, Category
from .models import Course

# Create your views here.
def index(req):
    context = {
        "courses": Course.objects.all()
    }

    return render(req, 'index.html', context)


def addcourse(req):
    Course.objects.create(name=req.POST['name'],description=req.POST['description'])

    return redirect('/')


def delcourse(req, id):
    context={
        "course": Course.objects.get(id=id)
    }
    req.session['del_course_id'] = id

    return render(req, 'delete_course.html', context)

def delcourse2(req):
    # Safety measure to prevent hacking delete
    if req.session['del_course_id']:
        Course.objects.get(id=req.session['del_course_id']).delete()
        del req.session['del_course_id']

    return redirect('/')