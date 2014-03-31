from django.db import models

class Social(models.Model):

    title = models.CharField(max_length=100, default='')
    github_url = models.URLField(blank=True, default='')
    linkedin_url = models.URLField(blank=True, default='')
    twitter_url = models.URLField(blank=True, default='')
    facebook_url = models.URLField(blank=True, default='')
