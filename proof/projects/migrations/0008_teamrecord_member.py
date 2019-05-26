# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-26 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_remove_teamrecord_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamrecord',
            name='member',
            field=models.ManyToManyField(related_name='team_record', to=settings.AUTH_USER_MODEL),
        ),
    ]
