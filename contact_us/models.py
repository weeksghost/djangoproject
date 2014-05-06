from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    recipient = models.EmailField()

    def __unicode__(self):
        return self.name
