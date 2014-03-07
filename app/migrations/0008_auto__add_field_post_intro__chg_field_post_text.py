# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.intro'
        db.add_column(u'app_post', 'intro',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Post.text'
        db.alter_column(u'app_post', 'text', self.gf('djangocms_text_ckeditor.fields.HTMLField')())

    def backwards(self, orm):
        # Deleting field 'Post.intro'
        db.delete_column(u'app_post', 'intro')


        # Changing field 'Post.text'
        db.alter_column(u'app_post', 'text', self.gf('django.db.models.fields.TextField')())

    models = {
        u'app.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['cms.CMSPlugin']},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '6'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'floating': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '5'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '640'}),
            'padding': ('django.db.models.fields.PositiveIntegerField', [], {'default': '20'}),
            'src': ('pyuploadcare.dj.models.ImageField', [], {}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '640'})
        },
        u'app.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('pyuploadcare.dj.models.ImageField', [], {}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '142', 'blank': 'True'}),
            'text': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '142'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['app']