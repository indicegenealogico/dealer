# Generated by Django 4.1 on 2022-08-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0003_car_description_alter_car_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
