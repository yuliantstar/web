# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import os

site = "http://127.0.0.1:8000/"

# Create your views here.
def index(request):
	content = {'content' : "index", 'site' : site}
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)
	#return render(request, template, {})
	
def my_diary(request):
		
	path = os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(path, 'templates\diary')
	files = os.listdir(path)
	
	title = []
	date = []
	for file in files[1:]:
		if not file.endswith('.py'):
			new_path = os.path.join(path, file)
			title.append(open(new_path).readlines()[4])
			date.append(open(new_path).readlines()[7])
		
	#return HttpResponse(date)
	
	#return HttpResponse(files[1:])
	content = {
		'content' : "diary",
		'sub_page' : "none",
		
		'site' : site, 
		'pages' : files[1:],
		'title' : title,
		'date' : date
	}
		
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)

def my_diary_page(request, page_diary):
	#return HttpResponse(new_path)
	
	new_path = os.path.join("diary/", page_diary.replace("/", ""))
	content = {
		'content' : "diary",
		'sub_page' : new_path,
		
		'site' : site, 
	}
		
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)

		
	
def electronic(request):
	content = {'content' : "electronic", 'site' : site}
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)
	
def computer(request):
	content = {'content' : "computer", 'site' : site}
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)
	
def about_me(request):
	content = {'content' : "about_me", 'site' : site}
	template = 'index.html'
	
	return render_to_response(
		template,
		content,
		RequestContext(request),
	)
