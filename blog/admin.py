# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Article, Author
# Register your models here.



class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name')

    def author_name(self,obj):
        return u'%s'%obj.author.name


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

#admin.site.register(Article)
#admin.site.register(Author)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article, BlogPostAdmin)