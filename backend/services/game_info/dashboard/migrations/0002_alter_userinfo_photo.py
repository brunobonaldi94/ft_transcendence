# Generated by Django 5.0.1 on 2024-04-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/img/avatar_user_icon2.png', null=True, upload_to='localhost:3000/static/src/img/'),
        ),
    ]