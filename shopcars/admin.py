from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from .models import *
from django import forms

# Register your models here.


class CarsAdminForm(forms.ModelForm):
    car_desription = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Cars
        fields = '__all__'


class CarsAdmin(admin.ModelAdmin):
    form = CarsAdminForm
    list_display = ('id', 'car_brand', 'car_model', 'car_country', 'car_price', 'photo', 'car_desription',
                    'car_relase_date', 'category', 'is_published')
    list_display_links = ('id', 'car_brand', 'category')
    search_fields = ('car_brand', 'car_model', 'car_price', 'category')
    list_filter = ('car_brand', 'car_model', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Category, CategoryAdmin)
