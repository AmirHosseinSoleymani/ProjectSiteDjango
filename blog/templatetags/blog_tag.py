
import random
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



@register.simple_tag()
def relatedPost(idx):
    time_now = timezone.now()
    post = Post.objects.get(id=idx)
    categories = post.category.all()
    relposts = Post.objects.filter(category__in=categories, status=True, published_date__lte=time_now).exclude(id=idx)
    relposts = list(set(relposts))
    random_posts = random.sample(relposts, 3)
    return random_posts