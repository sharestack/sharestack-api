# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("techs", "0003_auto__add_component"),
    )

    def forwards(self, orm):
        # Adding M2M table for field components on 'Instance'
        m2m_table_name = db.shorten_name(u'machines_instance_components')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('instance', models.ForeignKey(orm[u'machines.instance'], null=False)),
            ('component', models.ForeignKey(orm[u'techs.component'], null=False))
        ))
        db.create_unique(m2m_table_name, ['instance_id', 'component_id'])


    def backwards(self, orm):
        # Removing M2M table for field components on 'Instance'
        db.delete_table(db.shorten_name(u'machines_instance_components'))


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
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['techs.Component']", 'symmetrical': 'False', 'blank': 'True'}),
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
            'activation_token': ('django.db.models.fields.CharField', [], {'default': "'9d817d91-7f7b-4219-ab77-1181a48c1734'", 'max_length': '40', 'blank': 'True'}),
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
            'reset_password_token': ('django.db.models.fields.CharField', [], {'default': "'921caee7-ca78-4ed8-a758-6316ba4ba694'", 'max_length': '40', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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

    complete_apps = ['machines']