from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin as lrg
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm, UserLoginForms, UserRegistration, CarsForm


# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = UserRegistration()

    return render(request, 'shopcars/registr.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForms(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForms()
    return render(request, 'shopcars/login.html', {"form": form})


def userlogout(request):
    logout(request)
    return redirect('login')


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subjects'], form.cleaned_data['content'], 'djangobekov2022@gmail.com',
                             ['simalina554@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
            else:
                messages.error(request, 'Ошибка отправки письма!')

        else:
            messages.error(request, 'Ошибка!')
    else:
        form = ContactForm()

    return render(request, "shopcars/contact.html", {"form": form})


class HomePage(ListView):
    model = Cars
    template_name = 'shopcars/home_cars_list.html'
    context_object_name = 'carsAll'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Cars.objects.filter(is_published=True).select_related('category')


class CategoryView(ListView):
    model = Cars
    template_name = 'shopcars/home_cars_category.html'
    context_object_name = 'carsAll'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Cars.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class CarsView(DetailView):
    model = Cars
    context_object_name = 'cars_item'


class AddCars(CreateView):
    form_class = CarsForm
    model = Cars
    template_name = 'shopcars/create_cars.html'
    success_url = reverse_lazy('home')
    raise_exception = True


def aboutus(request):
    title = 'Страница о Нас! Рады вас приветствовать!'
    content = {'title': title}
    return render(request, template_name="shopcars/about.html", context=content)


