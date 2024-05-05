from django.contrib import sitemaps
from django.urls import reverse

class Staticviewsitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def item(self):
        return ['pages:index','pages:contact','pages:about']
    
    def location (self,item):
        return reverse(item)