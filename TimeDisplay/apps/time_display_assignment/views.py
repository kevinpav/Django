# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(req):
    context = {
        "sysdate": datetime.datetime.now().strftime("%b %d, %Y"),
        "systime": datetime.datetime.now().strftime("%I:%M %p")
    }
    return render(req, 'date.html', context)
