# Generated by Django 4.0.5 on 2022-09-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auction_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='listings',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='auction',
            name='message',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='auction',
            name='settings',
            field=models.JSONField(default=dict),
        ),
    ]
