# Generated by Django 5.0 on 2023-12-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dob',
            field=models.TextField(default=True),
        ),
    ]
