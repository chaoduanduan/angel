# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cart'
        db.create_table(u'carts_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'carts', ['Cart'])

        # Adding M2M table for field products on 'Cart'
        m2m_table_name = db.shorten_name(u'carts_cart_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cart', models.ForeignKey(orm[u'carts.cart'], null=False)),
            ('carinfo', models.ForeignKey(orm[u'productions.carinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cart_id', 'carinfo_id'])


    def backwards(self, orm):
        # Deleting model 'Cart'
        db.delete_table(u'carts_cart')

        # Removing M2M table for field products on 'Cart'
        db.delete_table(db.shorten_name(u'carts_cart_products'))


    models = {
        u'carts.cart': {
            'Meta': {'object_name': 'Cart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['productions.CarInfo']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'productions.carinfo': {
            'Meta': {'unique_together': "(('model', 'slug'),)", 'object_name': 'CarInfo'},
            'dealer': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'exterior_color': ('django.db.models.fields.CharField', [], {'default': "'Black'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interior_color': ('django.db.models.fields.CharField', [], {'default': "'Black'", 'max_length': '10'}),
            'mileage': ('django.db.models.fields.IntegerField', [], {}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productions.CarModel']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '8000.0', 'max_digits': '10', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vin_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '17'})
        },
        u'productions.carmodel': {
            'Meta': {'object_name': 'CarModel'},
            'additional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_Style': ('django.db.models.fields.CharField', [], {'default': "'SUV'", 'max_length': '60'}),
            'cylinder_and_Rotors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'doors': ('django.db.models.fields.CharField', [], {'default': "'4'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'drivetrain': ('django.db.models.fields.CharField', [], {'default': "'Front-Wheel'", 'max_length': '120'}),
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'fuel_Type': ('django.db.models.fields.CharField', [], {'default': "'Gas'", 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'gears': ('django.db.models.fields.IntegerField', [], {'default': '6'}),
            'horsepower': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liter': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '4'}),
            'mPG': ('django.db.models.fields.IntegerField', [], {}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'transmission': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weights': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['carts']