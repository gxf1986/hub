# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 06:06
from __future__ import unicode_literals

import components.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0003_auto_20160129_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, help_text='Date/time that this snapshot was created', null=True)),
                ('file', models.FileField(blank=True, help_text='File (.tar.gz) for this snapshot', null=True, upload_to=components.models.snapshot_upload_to)),
                ('component', models.ForeignKey(blank=True, help_text='Component that this snapshot is for', null=True, on_delete=django.db.models.deletion.CASCADE, to='components.Component')),
                ('user', models.ForeignKey(blank=True, help_text='User that created this snapshot', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]