# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-19 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travelPyLands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_perex', models.TextField()),
                ('hotel_desc', models.TextField()),
                ('hotel_lat', models.FloatField()),
                ('hotel_lng', models.FloatField()),
                ('hotel_rate', models.DecimalField(decimal_places=10, max_digits=11)),
                ('hotel_low_image', models.CharField(max_length=400)),
                ('hotel_high_image', models.CharField(max_length=400)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelPyLands.City')),
            ],
        ),
    ]
