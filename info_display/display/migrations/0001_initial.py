# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SubscriberCount'
        db.create_table('display_subscribercount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_subscribers', self.gf('django.db.models.fields.IntegerField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('display', ['SubscriberCount'])

        # Adding model 'YesterdaysSignupsCount'
        db.create_table('display_yesterdayssignupscount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscribers', self.gf('django.db.models.fields.IntegerField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('display', ['YesterdaysSignupsCount'])


    def backwards(self, orm):
        
        # Deleting model 'SubscriberCount'
        db.delete_table('display_subscribercount')

        # Deleting model 'YesterdaysSignupsCount'
        db.delete_table('display_yesterdayssignupscount')


    models = {
        'display.subscribercount': {
            'Meta': {'object_name': 'SubscriberCount'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_subscribers': ('django.db.models.fields.IntegerField', [], {})
        },
        'display.yesterdayssignupscount': {
            'Meta': {'object_name': 'YesterdaysSignupsCount'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscribers': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['display']
