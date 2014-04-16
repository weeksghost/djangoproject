from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=250)
    caption = models.TextField(blank=True)
    photographer = models.CharField(max_length=100, blank=True)
    copyright = models.CharField(max_length=100, default="", blank=True)
    image = models.ImageField(upload_to='photo/image/')
    small_image = models.ImageField(upload_to='photo/small_image/', blank=True)

    def __unicode__(self):
        return self.name


class PhotoOrder(models.Model):
    photo = models.ForeignKey('photos.Photo')
    gallery = models.ForeignKey('photos.Gallery')
    order = models.IntegerField(default=0)


class Gallery(models.Model):
    name = models.CharField(max_length=250)
    photos = models.ManyToManyField('photos.Photo', through='photos.PhotoOrder')

    def ordered_photos(self):
        return self.photos.order_by('photoorder__order')

    class Meta:
        verbose_name_plural = 'galleries'

    def __unicode__(self):
        return self.name
