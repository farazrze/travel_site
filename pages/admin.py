from django.contrib import admin
from pages.models import Contact




class Contactadmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_date')
    list_filter = ('name','email')
    search_fields = ['name','subject','email','message']




admin.site.register(Contact,Contactadmin)
