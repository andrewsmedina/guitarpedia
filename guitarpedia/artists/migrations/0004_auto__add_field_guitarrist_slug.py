# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Guitarrist.slug'
        db.add_column('artists_guitarrist', 'slug', self.gf('django.db.models.fields.SlugField')(default='foo', max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Guitarrist.slug'
        db.delete_column('artists_guitarrist', 'slug')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['artists']
