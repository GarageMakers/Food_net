# Generated by Django 4.0.2 on 2022-04-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='photo_path',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]