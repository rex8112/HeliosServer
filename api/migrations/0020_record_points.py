# Generated by Django 4.0.5 on 2022-10-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_auction_listings_alter_auction_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]