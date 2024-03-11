from django.contrib import admin
from blog.models import post


class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    #fields = ('title','content')
    #exclude = ('status',)
    list_display = ('id','title','created_date')
    list_filter = ('status','created_date')
    search_fields = ('title','content')




admin.site.register (post,Postadmin)
