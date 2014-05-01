from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'portfolio.views.portfolio_list', name='portfolio'),
)
