# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random

# from http://www.finestquotes.com Kill Bill Vol1, Vol2
ITEMLIST = ["Wiggle your big toe.",
            "What she lacks in age, she makes up for in madness.",
            "Okinawa. One way.",
            "I might never have liked you, point in fact I despised you. But that shouldn't suggest I don't respect you.",
            "Funny. You like samurai swords, I like baseball.",
            "So, O-Ren...any more subordinates for me to kill?",
            "It's mercy, compassion, and forgiveness I lack. Not rationality.",
            "My Pussy Wagon died on me.",
            "I was wondering, just between us girls, what did you say to Pai Mei to make him snatch out your eye?",
            "I'm a killer. A murdering bastard, you know that. And there are consequences to breaking the heart of a murdering bastard."]

def get_random_items(numItems):
    randomList = []
    for i in xrange(numItems):
        # Could use numpy here, for more selection options
        randomList.append(random.choice(ITEMLIST)) 
    # Could use random.sample But it chokes if numItems > ITEMLIST
    # return random.sample(ITEMLIST, numItems)
    return randomList

# Create your views here.
def index(req):

    return render(req, 'index.html')

def results(req):
    # print("POST.mynumber: {}".format(req.POST['mynumber']))
    if req.POST['mynumber'] == '':
        return redirect('/')

    myNumber = int(req.POST['mynumber'])
    if myNumber < 1:
        return redirect('/')
    # else:
    #     print("myNumber= {}".format(myNumber))

    # Initialize or set the session.colors to []
    req.session['items'] = get_random_items(myNumber)

    return render(req, 'results.html')