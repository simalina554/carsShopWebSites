from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', aboutus, name='aboutus'),
    path('contact/', contactus, name='contactus'),
    path('category/<int:category_id>', get_category, name='category'),
    path('cars/<int:cars_id>', views_cars, name='views_cars'),
    path('add_cars', add_cars, name='add_cars')
]
