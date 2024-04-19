
from django import template
from blog.models import *

register = template.Library()

@register.simple_tag
def get_posts_by_category(category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return posts
