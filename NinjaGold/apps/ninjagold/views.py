# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random, string

## Define RandomNum function here
def getRandomGold(minNum, maxNum):
    return random.randrange(minNum,maxNum+1)

# Create your views here.
def index(req):
    # Display index/form
    if 'myGold' not in req.session:
        req.session['myGold'] = 0
    if 'myActivity' not in req.session:
        req.session['myActivity'] = ""

    return render(req, 'index.html')

def process_money(req, route):
    # print("** {} **".format(route))
    # Check which route and process accordingly
    if route == 'farm':
        # 10-20 gold
        minedGold = getRandomGold(10,20)
        strAction = "Mined"
    elif route == 'cave':
        # 5-10 gold
        minedGold = getRandomGold(5,10)
        strAction = "Mined"
    elif route == 'house':
        # 2-5 gold
        minedGold = getRandomGold(2,5)
        strAction = "Mined"
    elif route == 'casino':
        # -50 to + 50 gold
        minedGold = getRandomGold(-50,50)
        if minedGold < 0:
            strAction = "Lost"
        else:
            strAction = "Won"
    elif route == 'reset':
        # Reset mining operations
        req.session['myGold'] = 0
        req.session['myActivity'] = ""
        return redirect('/')
    else:
        print "Nothing to do!"
        minedGold = 0

    req.session['myGold'] += minedGold
    actLog = strAction + " " + str(minedGold) + " gold from the " + route + "!\r\n"
    # Print a message if the player is busted
    if ((minedGold < 0) and (req.session['myGold'] < 0)):
        actLog += "  OH NOES!!!\r\n"
    # Append activity log
    req.session['myActivity'] += actLog

    return redirect('/')

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
