# Generated by Django 2.2.12 on 2020-04-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200131_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='hosts',
            field=models.TextField(blank=True, help_text='A space separated list of valid hosts for the account.Used for setting Content Security Policy headers when serving content for this account.', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='theme',
            field=models.TextField(blank=True, help_text='The name of the theme to use as the default when generating content for this account.', null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='logo',
            field=models.ImageField(blank=True, help_text='Logo for the account. Please use an image that is 100 x 100 px or smaller.', null=True, upload_to=''),
        ),
    ]
