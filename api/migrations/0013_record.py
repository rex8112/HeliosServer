# Generated by Django 4.0.5 on 2022-08-11 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_horse_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('earnings', models.BigIntegerField(default=0)),
                ('placing', models.IntegerField()),
                ('date', models.DateField()),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.horse')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.race')),
            ],
        ),
    ]
