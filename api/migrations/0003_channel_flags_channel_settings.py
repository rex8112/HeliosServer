# Generated by Django 4.0.5 on 2022-06-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_channels_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='flags',
            field=models.JSONField(default='[]'),
        ),
        migrations.AddField(
            model_name='channel',
            name='settings',
            field=models.JSONField(default='{}'),
        ),
    ]
