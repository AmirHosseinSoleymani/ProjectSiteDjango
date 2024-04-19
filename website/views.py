from django.shortcuts import render
from blog.models import *
from django.utils import timezone

def indexView(req):
    timeNow = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lte=timeNow).order_by('-published_date')
    cats = Category.objects.all()


    ctx = {
        'posts' : posts,
        'cats' : cats,
    }
    return render(req,'index.html',ctx)