from django import template
from django.db.models import *
from shopcars.models import Category, Cars

register = template.Library()


@register.simple_tag()
def find_category():
    allCategories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('cars')).filter(cnt__gt=0)
    return categories


@register.inclusion_tag('shopcars/list_categories.html')
def show_categories():
    categories = Category.objects.all()

    return {"categories": categories}
