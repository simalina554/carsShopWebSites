from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .forms import CarsForm
from .models import *




# Create your views here.



def hello(request):
    return HttpResponse("<h1>Hello</h1>")


def index(request):
    allCars = Cars.objects.all()
    content = {'carsAll': allCars, 'titleInHtml': 'Список всех машин'}
    return render(request, template_name='shopcars/index.html', context=content)


def get_category(request, category_id):
    cars = Cars.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    content = {'cars': cars, 'category': category}
    return render(request, "shopcars/category.html", content)


def aboutus(request):
    title = 'Страница о Нас! Рады вас приветствовать!'
    content = {'title': title, }
    return render(request, template_name="shopcars/about.html", context=content)


def contactus(request):
    title = 'Наши контакты'
    content = {'title': title, }
    return render(request, template_name="shopcars/about.html", context=content)


def views_cars(request, cars_id):
    # try:
    #     news_item = News.objects.get(pk=news_id)
    # except News.DoesNotExist:
    #     raise Http404("Такой новости не существует")
    cars_item = get_object_or_404(Cars, pk=cars_id)
    return render(request, "shopcars/cars.html", {'cars_item': cars_item})


def add_cars(request):
    if request.method == 'POST':
        form = Cars(request.POST)

        if form.is_valid():
            Cars.objects.create(**form.cleaned_data)
            return redirect('home')

    else:
        form = CarsForm()

    return render(request, 'shopcars/add_cars.html', {"form": form})
