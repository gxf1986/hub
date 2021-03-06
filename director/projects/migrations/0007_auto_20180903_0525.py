# Generated by Django 2.0.7 on 2018-09-03 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20180830_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='max_concurrent',
            new_name='sessions_concurrent',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='max_queue',
            new_name='sessions_queued'
        ),
        migrations.RenameField(
            model_name='project',
            old_name='max_sessions',
            new_name='sessions_total',
        ),

        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, help_text='Brief description of the project', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='key',
            field=models.TextField(blank=True, help_text='Key required to create sessions for this project', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False, help_text='Should this project be publicly visible?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='session_parameters',
            field=models.ForeignKey(blank=True, help_text='The parameters that defines sessions created for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.SessionParameters'),
        ),
        migrations.AlterField(
            model_name='project',
            name='token',
            field=models.TextField(blank=True, help_text='A token to identify this project (in URLs etc)', null=True, unique=True),
        ),

        migrations.RemoveField(
            model_name='sessionparameters',
            name='display_order',
        ),
        migrations.RemoveField(
            model_name='sessionparameters',
            name='is_system',
        ),
        migrations.RemoveField(
            model_name='sessionparameters',
            name='owner',
        ),
        migrations.AlterField(
            model_name='sessionparameters',
            name='cpu',
            field=models.FloatField(blank=True, default=1, help_text='CPU shares (out of 100 per CPU) allocated', null=True),
        ),
        migrations.AlterField(
            model_name='sessionparameters',
            name='memory',
            field=models.FloatField(blank=True, default=1, help_text='Gigabytes (GB) of memory allocated', null=True),
        ),
        migrations.AlterField(
            model_name='sessionparameters',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sessionparameters',
            name='timeout',
            field=models.IntegerField(blank=True, default=60, help_text='Minutes of inactivity before the session is terminated', null=True),
        ),

        migrations.RemoveField(
            model_name='source',
            name='address',
        ),
        migrations.RemoveField(
            model_name='source',
            name='creator',
        ),
    ]
