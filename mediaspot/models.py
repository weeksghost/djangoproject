from django.db import models
from django.conf import settings

MEDIASPOT_ROOT = getattr(settings, 'MEDIASPOT_ROOT', 'mediaspot')

class MediaFile(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=MEDIASPOT_ROOT)

    def size(self):
        try:
            return u'%s bytes' % self.file.size
        except OSError:
            return ''

    def get_absolute_url(self):
        return u'%s%s' % (settings.MEDIA_URL, self.file.name)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
