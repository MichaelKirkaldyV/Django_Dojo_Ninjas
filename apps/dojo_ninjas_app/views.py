# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, dojo_ninjas_app/index.html)

# Create your views here.
