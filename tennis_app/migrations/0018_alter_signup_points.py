# Generated by Django 4.2.4 on 2023-09-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0017_signup_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='points',
            field=models.IntegerField(default='0'),
        ),
    ]
