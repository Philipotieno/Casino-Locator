# Generated by Django 3.0.4 on 2020-03-06 06:34

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='loaction',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
