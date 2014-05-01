from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Work(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, default='')
    slug = models.SlugField(unique=True, max_length=255)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now())
    photo = models.ImageField(upload_to='portfolio/photo/', blank=True,)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return '/portfolio/%s' % self.slug
