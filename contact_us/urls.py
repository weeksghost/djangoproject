from django.conf.urls import url, patterns

from contact_us import views, forms


urlpatterns = patterns('',
    url(r'^$', views.ContactFormView.as_view(
        template_name="contact_us.html",
        form_class=forms.BasicContactForm,
    ), name="contact"),
    url(r'^thankyou/$', views.CompletedPage.as_view(), name="thankyou"),
)
