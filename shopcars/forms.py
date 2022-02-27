from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    subjects = forms.CharField(label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={"class": "form-control"}))
    captcha = CaptchaField(widget=CaptchaTextInput())


class UserLoginForms(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegistration(UserCreationForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars

        fields = ['car_brand', 'car_model', 'car_country', 'car_desription', 'car_price', 'photo',
                  'category', 'is_published']

        widgets = {
            'car_brand': forms.TextInput(attrs={"class": "form-control"}),
            'car_model': forms.TextInput(attrs={"class": "form-control"}),
            'car_country': forms.TextInput(attrs={"class": "form-control"}),
            'car_desription': forms.Textarea(attrs={"class": "form-control"}),
            'car_price': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"})
        }
