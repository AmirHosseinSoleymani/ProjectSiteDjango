
from django import template
from blog.models import *
from django.utils import timezone

register = template.Library()

@register.simple_tag
def get_posts_by_category(category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return posts


@register.simple_tag
def allCategories():
    cats = Category.objects.all()
    return cats


@register.simple_tag
def current_time():
    timeNow = timezone.now()
    return timeNow.date()