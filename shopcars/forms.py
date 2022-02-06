from django import forms
from .models import *


class CarsForm(forms.ModelForm):

    fields = ['car_brand', 'car_model', 'car_country', 'car_desription', 'car_price', 'car_relase_date', 'photo',
              'category']

    widgets = {
        'car_brand': forms.TextInput(attrs={"class": "form-control"}),
        'car_model': forms.TextInput(attrs={"class": "form-control"}),
        'car_country': forms.TextInput(attrs={"class": "form-control"}),
        'car_desription': forms.Textarea(attrs={"class": "form-control"}),
        'car_price': forms.TextInput(attrs={"class": "form-control"}),
        'car_relase_date': forms.TextInput(attrs={"class": "form-control"}),
        'category': forms.Select(attrs={"class": "form-control"})

    }

    # car_brand = forms.CharField(max_length=200, label='Бренд',
    #                             widget=forms.TextInput(attrs={"class": "form-control"}))
    # car_model = forms.CharField(max_length=200, label='Модель',
    #                             widget=forms.TextInput(attrs={"class": "form-control"}))
    # car_country = forms.CharField(max_length=200, label='Страна',
    #                               widget=forms.TextInput(attrs={"class": "form-control"}))
    # car_desription = forms.CharField(label='Текст', required=False,
    #                                  widget=forms.Textarea(attrs={"class": "form-control"}))
    # car_price = forms.CharField(max_length=200, label='Цена',
    #                             widget=forms.TextInput(attrs={"class": "form-control"}))
    # car_relase_date = forms.CharField(max_length=200, label='Дата',
    #                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    # # photo = forms.ImageField(upload_to='photos/%Y/%m/%d', default='', verbose_name='Фото', null=True)
    # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(),
    #                                   widget=forms.Select(attrs={"class": "form-control"}))
