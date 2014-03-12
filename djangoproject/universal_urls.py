from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'djangoproject.views.homepage', name='home'),

        (r'', include('sitemaps.urls')),
        (r'^robots\.txt$', include('robots.urls')),

        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),

        url(r'^contact/', include('contact_us.urls', namespace='contact_us')),
        url(r'^blog/', include('blog.urls')),
)
