from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        timeNow = timezone.now()
        return Post.objects.filter(status=True,published_date__lte=timeNow)

    def lastmod(self, obj):
        return obj.published_date