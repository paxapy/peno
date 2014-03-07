# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.image'
        db.alter_column(u'app_post', 'image', self.gf('pyuploadcare.dj.models.ImageField')())

    def backwards(self, orm):

        # Changing field 'Post.image'
        db.alter_column(u'app_post', 'image', self.gf('pyuploadcare.dj.models.FileField')())

    models = {
        u'app.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('pyuploadcare.dj.models.ImageField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '142', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '142'})
        }
    }

    complete_apps = ['app']