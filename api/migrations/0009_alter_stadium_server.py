# Generated by Django 4.0.5 on 2022-08-02 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_stadium_race_horse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='server',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='stadium', serialize=False, to='api.server'),
        ),
    ]