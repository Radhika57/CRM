# Generated by Django 4.0.2 on 2023-06-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_flight_booking_departure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight_booking',
            name='departure',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight_booking',
            name='return_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]