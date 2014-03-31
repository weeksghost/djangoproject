# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Social'
        db.create_table(u'social_social', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('github_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('linkedin_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('twitter_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'social', ['Social'])


    def backwards(self, orm):
        # Deleting model 'Social'
        db.delete_table(u'social_social')


    models = {
        u'social.social': {
            'Meta': {'object_name': 'Social'},
            'github_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['social']