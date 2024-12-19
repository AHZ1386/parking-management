# Generated by Django 5.1.2 on 2024-12-18 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(max_length=8)),
                ('car_type', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=50)),
                ('enter_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(auto_now=True)),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='parking.parking')),
            ],
        ),
    ]
