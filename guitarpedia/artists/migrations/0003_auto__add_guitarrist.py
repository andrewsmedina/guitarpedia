# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Guitarrist'
        db.create_table('artists_guitarrist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date_of_birthday', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('artists', ['Guitarrist'])


    def backwards(self, orm):
        
        # Deleting model 'Guitarrist'
        db.delete_table('artists_guitarrist')


    models = {
        'artists.band': {
            'Meta': {'object_name': 'Band'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'artists.guitarrist': {
            'Meta': {'object_name': 'Guitarrist'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_of_birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['artists']
