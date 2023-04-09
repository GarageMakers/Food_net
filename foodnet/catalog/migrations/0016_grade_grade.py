# Generated by Django 4.0.2 on 2022-08-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=1),
            preserve_default=False,
        ),
    ]