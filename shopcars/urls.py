from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', aboutus, name='aboutus'),
    path('contact/', contactus, name='contactus'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', CategoryView.as_view(extra_context={'title': 'Название заголовка'}),
         name='category'),
    path('cars/<int:pk>', CarsView.as_view(), name='views_cars'),
    # path('add_cars', add_cars, name='add_cars')
    path('create_cars', AddCars.as_view(), name='create_cars'),
    path('registr/', registration, name='registr'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout')
]
