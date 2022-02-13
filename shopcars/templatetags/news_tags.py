from django import template
from django.db.models import *
from shopcars.models import Category, Cars

register = template.Library()


@register.simple_tag()
def find_category():
    categories = Category.objects.annotate(cnt=Count('findcars')).filter(cnt__gt=0)
    return Category.objects.all()


@register.simple_tag()
def show_categories():
    categories = Category.objects.annotate(cnt=Count('findcars')).filter(cnt__gt=0)
