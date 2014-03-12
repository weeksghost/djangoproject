from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'blog.views.blog_list', name='blog'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post', name='post'),
)
