# Generated by Django 4.0.2 on 2022-08-08 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_grade_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('user',)},
        ),
    ]
