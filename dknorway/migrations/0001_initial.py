# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fylke'
        db.create_table(u'dknorway_fylke', (
            ('nr', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('navn', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'dknorway', ['Fylke'])

        # Adding model 'Kommune'
        db.create_table(u'dknorway_kommune', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kode', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('navn', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'dknorway', ['Kommune'])

        # Adding model 'PostSted'
        db.create_table(u'dknorway_poststed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postnummer', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('poststed', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('kommune', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dknorway.Kommune'], null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dknorway', ['PostSted'])


    def backwards(self, orm):
        # Deleting model 'Fylke'
        db.delete_table(u'dknorway_fylke')

        # Deleting model 'Kommune'
        db.delete_table(u'dknorway_kommune')

        # Deleting model 'PostSted'
        db.delete_table(u'dknorway_poststed')


    models = {
        u'dknorway.fylke': {
            'Meta': {'ordering': "['nr']", 'object_name': 'Fylke'},
            'navn': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'})
        },
        u'dknorway.kommune': {
            'Meta': {'ordering': "['kode']", 'object_name': 'Kommune'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'navn': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'dknorway.poststed': {
            'Meta': {'object_name': 'PostSted'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kommune': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dknorway.Kommune']", 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'postnummer': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'poststed': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['dknorway']