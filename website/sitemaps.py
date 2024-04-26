from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        print('❤️❤️❤️❤️')
        return ['website:index']
    
    def location(self,item):
        print('❤️')
        return reverse(item)