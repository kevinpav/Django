# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .forms import UsernameForm
# from .models import Book, Author, Category
from .models import User

# class UsernameForm(forms.Form):
#     username = forms.CharField(min_length=9, max_length=25)

# Create your views here.
def index(req):
    # form = UsernameForm()
    context = {
        "form": UsernameForm(),
        "users": User.objects.all()
    }

    return render(req, 'index.html', context)


def addusername(req):
    # Course.objects.create(name=req.POST['name'],description=req.POST['description'])
    if req.method == "POST":
        result = UsernameForm(req.POST)

        if not result.is_valid():
            context = {
                "form": result,
                "users": User.objects.all()
            }
            # print result.errors
            return render(req, 'index.html', context)

        result.save()

    return redirect('/')


# def delcourse(req, id):
#     context={
#         "course": Course.objects.get(id=id)
#     }
#     req.session['del_course_id'] = id

#     return render(req, 'delete_course.html', context)

# def delcourse2(req):
#     # Safety measure to prevent hacking delete
#     if req.session['del_course_id']:
#         Course.objects.get(id=req.session['del_course_id']).delete()
#         del req.session['del_course_id']

#     return redirect('/')