# Generated by Django 2.2.7 on 2020-01-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200107_1723'),
        ('projects', '0021_auto_20191219_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, help_text='An identifier for the Project, used in the URL. It must be unique for the account.', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('slug', 'account')},
        )
    ]
