# Generated by Django 4.0.5 on 2022-06-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_channel_flags_channel_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='flags',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='channel',
            name='settings',
            field=models.JSONField(default=dict),
        ),
    ]
