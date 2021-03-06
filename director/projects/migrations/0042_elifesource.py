# Generated by Django 2.2.12 on 2020-05-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_auto_20200414_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElifeSource',
            fields=[
                ('source_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Source')),
                ('article', models.IntegerField(help_text='The article number.')),
                ('version', models.IntegerField(blank=True, help_text='The article version. If blank, defaults to the latest.', null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('projects.source',),
        ),
    ]
