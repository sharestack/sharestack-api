# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Instance.ram'
        db.add_column(u'machines_instance', 'ram',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.cpu'
        db.add_column(u'machines_instance', 'cpu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.hdd'
        db.add_column(u'machines_instance', 'hdd',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.instance_type'
        db.add_column(u'machines_instance', 'instance_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.provider'
        db.add_column(u'machines_instance', 'provider',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.provider_name'
        db.add_column(u'machines_instance', 'provider_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Instance.description'
        db.add_column(u'machines_instance', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Instance.ram'
        db.delete_column(u'machines_instance', 'ram')

        # Deleting field 'Instance.cpu'
        db.delete_column(u'machines_instance', 'cpu')

        # Deleting field 'Instance.hdd'
        db.delete_column(u'machines_instance', 'hdd')

        # Deleting field 'Instance.instance_type'
        db.delete_column(u'machines_instance', 'instance_type')

        # Deleting field 'Instance.provider'
        db.delete_column(u'machines_instance', 'provider')

        # Deleting field 'Instance.provider_name'
        db.delete_column(u'machines_instance', 'provider_name')

        # Deleting field 'Instance.description'
        db.delete_column(u'machines_instance', 'description')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'machines.instance': {
            'Meta': {'object_name': 'Instance'},
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_type': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'stack': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['machines.Stack']"})
        },
        u'machines.stack': {
            'Meta': {'object_name': 'Stack'},
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'collaboration_stack'", 'blank': 'True', 'to': u"orm['members.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_stack'", 'to': u"orm['members.User']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sharelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'members.user': {
            'Meta': {'object_name': 'User'},
            'activation_token': ('django.db.models.fields.CharField', [], {'default': "'7f8276cc-3a77-43d6-80f9-b4bfeb45a665'", 'max_length': '40', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gravatar': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reset_password_token': ('django.db.models.fields.CharField', [], {'default': "'aef9f13d-07f9-4e6c-a367-3c3cea36c2ea'", 'max_length': '40', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['machines']