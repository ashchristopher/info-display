# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'MainMessage'
        db.delete_table('display_mainmessage')

        # Adding model 'Subscribers'
        db.create_table('display_subscribers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_subscribers', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('display', ['Subscribers'])


    def backwards(self, orm):
        
        # Adding model 'MainMessage'
        db.create_table('display_mainmessage', (
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('display', ['MainMessage'])

        # Deleting model 'Subscribers'
        db.delete_table('display_subscribers')


    models = {
        'display.subscribers': {
            'Meta': {'object_name': 'Subscribers'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_subscribers': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['display']
