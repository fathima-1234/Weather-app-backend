# Generated by Django 5.0.2 on 2024-02-21 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_weather_coordinate_weather_country_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='wind_speed',
        ),
    ]
