# Generated by Django 4.1.7 on 2023-03-24 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0008_alter_customer_pan_alter_customer_passport"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_customer",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]