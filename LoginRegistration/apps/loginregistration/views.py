# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
# from .models import Book, Author, Category
from .models import User

# Create your views here.
def index(req):
    context = {
        "form": RegisterForm(),
        "loginform": LoginForm(),
        "users": User.objects.all()
    }

    return render(req, 'index.html', context)

def login(req):
    # print("req: {}".format(req))
    if req.method == "POST":
        result = LoginForm(req.POST)
        print("login.result: {}".format(result))
        if result.is_valid():
            context = {
                "user": User.objects.get(email=req.POST['email'].lower())
            }
            return render(req, 'success.html', context)

    context = {
        "form": result,
        "loginform": LoginForm(),
        "users": User.objects.all()
    }
    return render(req, 'index.html', context)

def register(req):
    # Course.objects.create(name=req.POST['name'],description=req.POST['description'])
    if req.method == "POST":
        result = RegisterForm(req.POST)

        if result.is_valid():
            # This broke the form. TODO: figure out a way to lower() the email
            # result['email'] = req.POST['email'].lower()
            newuser = result.save()
            # print("newuser= {}".format(newuser))
            uid = int(newuser.id)
            req.session['uid'] = uid
            # print("uid= {}".format(uid))
            context = {
                "user": User.objects.get(id=uid)
            }
            return render(req, 'success.html', context)
        else:
            context = {
                "form": result,
                "loginform": LoginForm(),
                "users": User.objects.all()
            }
            # print result.errors
            return render(req, 'index.html', context)

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