# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20170611_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='products.Product'),
            preserve_default=False,
        ),
    ]