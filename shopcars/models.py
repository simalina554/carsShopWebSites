from django.db import models
from django.urls import reverse

# Create your models here.


class Cars(models.Model):
    car_brand = models.CharField(max_length=200, verbose_name='Бренд')
    car_model = models.TextField(blank=True, verbose_name='Модель')
    car_country = models.TextField(blank=True, verbose_name='Страна')
    car_desription = models.TextField(blank=True, verbose_name='Описание')
    car_price = models.CharField(max_length=100, verbose_name='Цена', null=True)
    car_relase_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', null=True, default='')

    def get_absolute_url(self):
        return "/cars/%i" % self.id

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['car_relase_date']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return "/category/%i" % self.id

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
