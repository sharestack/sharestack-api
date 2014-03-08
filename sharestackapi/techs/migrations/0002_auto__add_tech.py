# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tech'
        db.create_table(u'techs_tech', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('open_source', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('repo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'techs', ['Tech'])

        # Adding M2M table for field types on 'Tech'
        m2m_table_name = db.shorten_name(u'techs_tech_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tech', models.ForeignKey(orm[u'techs.tech'], null=False)),
            ('techtype', models.ForeignKey(orm[u'techs.techtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tech_id', 'techtype_id'])

        # Adding M2M table for field tech_components on 'Tech'
        m2m_table_name = db.shorten_name(u'techs_tech_tech_components')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_tech', models.ForeignKey(orm[u'techs.tech'], null=False)),
            ('to_tech', models.ForeignKey(orm[u'techs.tech'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_tech_id', 'to_tech_id'])


    def backwards(self, orm):
        # Deleting model 'Tech'
        db.delete_table(u'techs_tech')

        # Removing M2M table for field types on 'Tech'
        db.delete_table(db.shorten_name(u'techs_tech_types'))

        # Removing M2M table for field tech_components on 'Tech'
        db.delete_table(db.shorten_name(u'techs_tech_tech_components'))


    models = {
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