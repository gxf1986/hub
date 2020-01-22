# Generated by Django 2.2.7 on 2020-01-21 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200121_2117'),
    ]

    operations = [
        migrations.RunSQL(
            "UPDATE accounts_account SET name=slug"
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.SlugField(help_text='Name of the account', unique=True),
        ),
    ]
