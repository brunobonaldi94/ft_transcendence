# Generated by Django 5.0.1 on 2024-03-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_signinupoauth42dto_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="signinupoauth42dto",
            options={"managed": False},
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
