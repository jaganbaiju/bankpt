# Generated by Django 5.0 on 2023-12-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp2', '0005_remove_data_material_data_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
    ]
