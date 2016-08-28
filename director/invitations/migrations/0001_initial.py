# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-28 07:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import invitations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0009_component_environ'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitee', models.CharField(help_text='An identifier for the person receiving the invitation. Usually an email address', max_length=255)),
                ('platform', models.CharField(choices=[('email', 'Email')], default='email', help_text='The platform for sending the invitation.', max_length=16)),
                ('subject', models.CharField(help_text='The subject of the invitation', max_length=255)),
                ('message', models.TextField(help_text='The message of the invitation')),
                ('path', models.CharField(help_text='The path to redirect the intivtee to after acceptance', max_length=255)),
                ('string', models.CharField(default=invitations.models.invitation_create_string, help_text='A string of character used to identify this invitation', max_length=64, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Time that this invitation was created')),
                ('sent', models.DateTimeField(blank=True, help_text='Time that this invitation was sent to invitee', null=True)),
                ('expiry', models.FloatField(default=7, help_text='Number of days until this invitation expires. Can be fractional e.g. 0.2')),
                ('accepted', models.DateTimeField(blank=True, help_text='Time that this invitation was accepted by the invitee', null=True)),
                ('accepter', models.ForeignKey(help_text='User who accepted the invitation', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations_accepted', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ForeignKey(help_text='User giving the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_given', to=settings.AUTH_USER_MODEL)),
                ('key', models.ForeignKey(help_text='The access key to be given to the invitee', on_delete=django.db.models.deletion.CASCADE, related_name='invitation_keys', to='components.Key')),
            ],
        ),
    ]
