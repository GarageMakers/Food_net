# Generated by Django 4.0.2 on 2022-04-01 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_step_photo_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='photo',
        ),
    ]
