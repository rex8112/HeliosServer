# Generated by Django 4.0.5 on 2022-08-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_horse_server_alter_race_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='bets',
            field=models.JSONField(default=list),
        ),
    ]