# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)


class Article(models.Model):
    title = models.CharField(max_length=200)
    title_id = models.AutoField(primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(Author)