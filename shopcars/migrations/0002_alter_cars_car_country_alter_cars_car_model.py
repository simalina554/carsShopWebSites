# Generated by Django 4.0.2 on 2022-02-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_country',
            field=models.CharField(max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='car_model',
            field=models.CharField(max_length=200, verbose_name='Модель'),
        ),
    ]
