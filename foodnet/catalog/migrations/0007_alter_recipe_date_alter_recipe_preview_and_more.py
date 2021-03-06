# Generated by Django 4.0.2 on 2022-05-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_visitor_reg_date_visitor_isbanned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preview',
            field=models.ImageField(upload_to='../images'),
        ),
        migrations.AlterField(
            model_name='step',
            name='text_field',
            field=models.TextField(max_length=300),
        ),
    ]
