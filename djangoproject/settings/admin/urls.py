from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from djangoproject.universal_urls import urlpatterns

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/logout/$', 'base.views.broadway_logout', name='logout'),
    #(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', {'is_admin_site': True}, 'admin_password_reset'),
    #url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    #url(r'^admin/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    #url(r'^admin/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)
