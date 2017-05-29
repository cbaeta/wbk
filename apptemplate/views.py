# -*- coding: utf-8 -*-
# Original
from __future__ import unicode_literals
from django.shortcuts import render

# cbaeta
#from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def index(request):
	return render(request, 'apptemplate/index.html', {
		'var': 12345,
		})

def template(request):
	return render(request, 'apptemplate/template.html')


"""
def template(request, id):
	return HttpResponse('<p> Template Id {0}</p>'.format(id))	
"""

