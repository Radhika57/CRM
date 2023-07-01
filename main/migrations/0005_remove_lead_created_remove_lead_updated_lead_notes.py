# Generated by Django 4.0.2 on 2023-06-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_customized_package_lead_customized_package_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='created',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='updated',
        ),
        migrations.AddField(
            model_name='lead',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]