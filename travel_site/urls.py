from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from ..pages.sitemaps import *

sitemaps = {
    'static':Staticviewsitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('blog/',include('blog.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contric.sitemaps.views.sitemap')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)