# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random, string

def random_word(len):
    sRandom = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in xrange(len)])
    print sRandom
    return sRandom

# Create your views here.
def index(req):
    if 'numtries' not in req.session:
        req.session['numtries'] = 0

    if req.method == "POST":
        #Generate was pressed so generate a random word
        req.session['randomword'] = random_word(14)
        req.session['numtries'] += 1

    return render(req, 'index.html')
