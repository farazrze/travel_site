from django.contrib import admin
from blog.models import *


class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    #fields = ('title','content')
    #exclude = ('status',)
    list_display = ('id','title','author','created_date')
    list_filter = ('status','created_date')
    search_fields = ('title','content')


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('name','approve','created_date')
    list_filter = ('post','approve')
    search_fields = ('name','post')

admin.site.register (Post,Postadmin)
admin.site.register (Category)
admin.site.register (Comment,CommentAdmin)
