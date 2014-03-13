from django.db import models
from django.utils.translation import ugettext_lazy as _


class FeaturedText(models.Model):
    active = models.BooleanField(default=False)
    featured_title = models.CharField(_('Featured Title'), max_length=20, help_text='20 character limit') 
    featured_subtitle = models.CharField(_('Featured Subtitle'), max_length=20, help_text='30 character limit')
    content = models.TextField(_('Subtitle'), blank=True, help_text='This is the main text on the homepage. 200 character limit')
    call_to_action = models.URLField(_('URL'), max_length=225, blank=True, default='', help_text='This for the BIG button on the homepage.')   

    def __unicode__(self):
        return self.featured_title

class HomeWidget(models.Model):
    first_title = models.CharField(_('Title'), max_length=20)
    first_text =  models.TextField(_('Text'), max_length=250, default='')

    second_title = models.CharField(_('Title'), max_length=20)
    second_text =  models.TextField(_('Text'), max_length=250, default='')

    third_title = models.CharField(_('Title'), max_length=20)
    third_text =  models.TextField(_('Text'), max_length=250, default='')

    def __unicode__(self):
        return "Home Widget Content" 

class FeaturedVideo(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(_('Video Title'), max_length=100, blank=True, default='', unique=True)
    embed_url = models.URLField(_('Embed Url'), blank=True, default='', unique=True)

    def __unicode__(self):
        return self.title
