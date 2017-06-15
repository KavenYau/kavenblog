# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.shortcuts import render

# Create your views here.
from blog.models import Article


def hello(request):
    # return HttpResponse('<h1>hello Kaven,offset:%s</h1>' % offset)
    name = 'Kaven'
    age = 18
    return render(request, 'hello.html', locals())


def index(request):
    d = date.today()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())

def blog(request,title_id):
    d = date.today()
    articles = Article.objects.all()
    title_id = int(title_id)
    return render(request, 'single.html', locals())