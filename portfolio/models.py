from django.db import models
from django.utils import timezone


class Supersize(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='portfolio/image', blank=True)
    photo_thumbnail = models.ImageField(upload_to='portfolio/image_thumbnail', blank=True)
    gallery = models.ForeignKey('photos.Gallery', null=True, blank=True)
