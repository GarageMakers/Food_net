# Generated by Django 4.0.2 on 2022-07-12 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_recipe_date_alter_recipe_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.visitor'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preview',
            field=models.ImageField(default='NULL', null=True, upload_to='uploads/previews/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='step',
            name='photo_path',
            field=models.ImageField(default='NULL', null=True, upload_to='uploads/steps/%Y/%m/%d/'),
        ),
    ]
