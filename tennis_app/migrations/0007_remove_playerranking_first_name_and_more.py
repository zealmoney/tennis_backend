# Generated by Django 4.2.4 on 2023-09-06 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0006_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerranking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='playerranking',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='PlayerRanking',
        ),
    ]
