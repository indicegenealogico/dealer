# Generated by Django 4.1 on 2022-08-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0006_alter_picture_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picture",
            name="picture",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
