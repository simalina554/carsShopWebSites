# Generated by Django 3.2.9 on 2022-01-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.TextField(max_length=200, verbose_name='Бренд')),
                ('car_model', models.TextField(blank=True, verbose_name='Модель')),
                ('car_country', models.TextField(blank=True, verbose_name='Страна')),
                ('car_desription', models.TextField(max_length=200, verbose_name='Описание')),
                ('car_relase_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]
