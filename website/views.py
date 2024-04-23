from django.shortcuts import render,redirect
from blog.models import *
from django.utils import timezone
from website.forms import *
from django.contrib import messages


def indexView(req):
    timeNow = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lte=timeNow).order_by('-published_date')
    cats = Category.objects.all()
    if req.method == 'POST':
        form = NewsForm(data=req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req,messages.SUCCESS,'Good,You can find out about the latest news from now')
        else:
            messages.add_message(req,messages.ERROR,'Oh,Sorry your information is not valid')

    form = NewsForm()

    ctx = {
        'posts' : posts,
        'cats' : cats,
        'form' : form
    }
    if req.method == 'POST':
        return redirect('/')
    return render(req,'index.html',ctx)



