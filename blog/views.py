
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

def blogView(req,**kwargs):
    timeNow = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lte=timeNow).order_by('-published_date') #just published posts
    most_viiw = posts.order_by('-counted_view')
    categories = Category.objects.all()
    
    if kwargs.get('cat_name') :
        posts = posts.filter(category__name = kwargs['cat_name'])
        return render(request=req,template_name='cat-fashion.html')
    
    if kwargs.get('author_uname'):
        posts = posts.filter(author__username=kwargs['author_uname'])

    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name=kwargs['tag_name'])


    # posts = Paginator(posts,1)
    # try:
    #     page_number = req.GET.get('page')
    #     posts = posts.get_page(page_number)

    # except PageNotAnInteger:
    #     posts = posts.get_page(1)
    # except EmptyPage:
    #     posts = posts.get_page(1)

    ctx = {
        'Posts' : posts,
        'cats' : categories ,
        'mposts' : most_viiw,
              }
    return render(request=req,template_name='blog.html',context=ctx)

def findNexPrevPosts(posts,post):
    index = 0
    for i in range(0,len(posts)):
        if posts[i].pk == post.id:
            index = i

    if index == 0 :
        nextpost = posts[index+1]
        prevpost = 'none'
    elif index+1 == len(posts):
        nextpost = 'none'
        prevpost = posts[index-1]
    else :
        nextpost = posts[index+1]
        prevpost = posts[index-1]
    return nextpost , prevpost


def blogSingleView(req,id):

    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req,messages.SUCCESS,'Your comment submited successfully')
        else:
            messages.add_message(req,messages.ERROR,'Your comment no submited OOPS!!')

            
    #post = Post.objects.get(id=id)
    # post = get_object_or_404(Post,pk=id,status=1)
    timeNow = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lte=timeNow)
    post = get_object_or_404(posts,pk=id,)
    post.counted_view += 1
    post.save()

    nextpost , prevpost = findNexPrevPosts(posts,post)

    comments = Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')

    form = CommentForm()

    ctx = {'post' : post , 'next' : nextpost , 'prev' : prevpost , 'comments' : comments , 'form' : form}
    return render(req,'blog-details.html',ctx)

# def blogCategory(req,cat_name):
#     timeNow = timezone.now()
#     posts = Post.objects.filter(status=True,published_date__lte=timeNow)
#     posts = posts.filter(category__name = cat_name)

#     ctx = {
#         'Posts' : posts,
#     }
#     return render(req,'blog/blog-home.html',ctx)

def blogSearch(req):
    # req.__dict__  --> django request objects and methodes showes

    posts = Post.objects.filter(status=True) 

    if req.method == 'GET':
        if get := req.GET.get('s'): #walrus in py
            posts = posts.filter(content__contains=get)
    ctx = {'Posts' : posts}
    return render(req,'blog/blog-home.html',ctx)
    
