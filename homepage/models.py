from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class FeaturedText(models.Model):
    active = models.BooleanField(default=False)
    featured_title = models.CharField(_('Featured Title'), max_length=20, help_text='20 character limit') 
    featured_subtitle = models.CharField(_('Featured Subtitle'), max_length=20, help_text='30 character limit')
    content = models.TextField(_('Subtitle'), blank=True, help_text='This is the main text on the homepage. 200 character limit')
    call_to_action = models.URLField(_('URL'), max_length=225, blank=True, default='', help_text='This for the BIG button on the homepage.')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.featured_title


class FeaturedVideo(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(_('Video Title'), max_length=100, blank=True, default='', unique=True)
    embed_url = models.URLField(_('Embed Url'), blank=True, default='', unique=True)
    created = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.title
