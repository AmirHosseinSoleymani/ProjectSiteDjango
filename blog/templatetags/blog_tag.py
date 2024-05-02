
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
def numCatWithPostId(id):
    comments = Comment.objects.filter(post=id)
    num = comments.__len__()
    return num


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
    if len(relposts) >= 3 :
        random_posts = random.sample(relposts, 3)
    else:
        random_posts = random.sample(relposts, 1)
    
    return random_posts

@register.simple_tag()
def lastComments(num=4):
    comments = Comment.objects.filter(approved=True).order_by('-created_date')[:num]
    return comments