# Generated by Django 4.0.2 on 2023-06-28 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_flight_booking_departure_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='customized_package',
            new_name='customized_Package',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='flight_booking',
            new_name='flight_Booking',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='hotel_booking',
            new_name='hotel_Booking',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='travel_insurance',
            new_name='travel_Insurance',
        ),
    ]
