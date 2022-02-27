# Generated by Django 4.0.2 on 2022-02-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128, verbose_name='Категория новости')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=200, verbose_name='Бренд')),
                ('car_model', models.TextField(blank=True, verbose_name='Модель')),
                ('car_country', models.TextField(blank=True, verbose_name='Страна')),
                ('car_desription', models.TextField(blank=True, verbose_name='Описание')),
                ('car_price', models.CharField(max_length=100, null=True, verbose_name='Цена')),
                ('car_relase_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('photo', models.ImageField(default=' ', upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shopcars.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['car_relase_date'],
            },
        ),
    ]
