from django.conf.urls import patterns, url

urlpatterns = patterns(
    'contact_us.views',
    url('^$', 'contact_form', name='contact'),
    url('^thankyou/$', 'thankyou', name='thankyou'),
)
