from django.conf.urls import patterns, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page

from blog.models import Post

blog_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'blog': GenericSitemap(blog_dict, priority=0.5),
}

urlpatterns = patterns(
    'django.contrib.sitemap.views',

    url(r'^sitemap\.xml$',
        cache_page(86400)(sitemap_views.index),
        {
            'sitemaps': sitemaps,
            'sitemap_url_name': 'sitemaps',
        }
        ),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        cache_page(86400)(sitemap_views.sitemap),
        {'sitemaps': sitemaps},
        name='sitemaps',
        ),
)
