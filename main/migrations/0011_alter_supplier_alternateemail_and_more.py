# Generated by Django 4.1.7 on 2023-03-24 11:49

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_hotel_user_sightseeing_user_supplier_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="alternateemail",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="alternatenumber",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=20, null=True, region=None
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="bankdetails",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="designation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=20, null=True, region=None
            ),
        ),
    ]