# Generated by Django 2.2.12 on 2020-05-18 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0042_elifesource'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlosSource',
            fields=[
                ('source_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Source')),
                ('article', models.TextField(help_text='The article doi.')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('projects.source',),
        ),
    ]
