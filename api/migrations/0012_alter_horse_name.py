# Generated by Django 4.0.5 on 2022-08-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_race_bets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]