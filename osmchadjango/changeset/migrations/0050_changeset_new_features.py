# Generated by Django 2.0.3 on 2018-04-23 19:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0049_auto_20180307_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='changeset',
            name='new_features',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]