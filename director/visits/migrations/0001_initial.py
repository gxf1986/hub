# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-12 02:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, help_text='Date/time of visit', null=True)),
                ('address', models.CharField(blank=True, help_text='Address of the component recording this visit', max_length=1024, null=True)),
                ('view', models.CharField(blank=True, help_text='View recording this visit', max_length=32, null=True)),
                ('scheme', models.CharField(blank=True, help_text='Scheme of the request (http or https usually)', max_length=8, null=True)),
                ('path', models.CharField(blank=True, help_text='Path to the requested page, not including the domain', max_length=1024, null=True)),
                ('method', models.CharField(blank=True, help_text='HTTP method used in the request', max_length=8, null=True)),
                ('type', models.CharField(blank=True, help_text='User agent type', max_length=3, null=True)),
                ('touchable', models.NullBooleanField(help_text='Is the user agent touch capable?')),
                ('device', models.CharField(blank=True, help_text='Device family', max_length=64, null=True)),
                ('browser', models.CharField(blank=True, help_text='Browser family', max_length=64, null=True)),
                ('browser_version', models.CharField(blank=True, help_text='Browser version', max_length=32, null=True)),
                ('referer', models.CharField(blank=True, help_text='The referring page, if any', max_length=1024, null=True)),
                ('ip', models.CharField(blank=True, help_text='The IP address of the client', max_length=15, null=True)),
                ('user', models.ForeignKey(blank=True, help_text='The authenticated user, if any', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]