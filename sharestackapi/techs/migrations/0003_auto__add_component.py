# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Component'
        db.create_table(u'techs_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('config', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tech', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['techs.Tech'])),
        ))
        db.send_create_signal(u'techs', ['Component'])


    def backwards(self, orm):
        # Deleting model 'Component'
        db.delete_table(u'techs_component')


    models = {
        u'techs.component': {
            'Meta': {'object_name': 'Component'},
            'config': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tech': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['techs.Tech']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'techs.tech': {
            'Meta': {'object_name': 'Tech'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'open_source': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'repo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tech_components': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['techs.Tech']", 'symmetrical': 'False', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['techs.TechType']", 'symmetrical': 'False', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'techs.techtype': {
            'Meta': {'object_name': 'TechType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['techs']