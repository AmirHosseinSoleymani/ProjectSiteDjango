from django.urls import path
from blog.views import *


app_name = "blog"

urlpatterns = [
    path('',blogView,name='index'),
    path('<int:id>',blogSingleView,name='blog-single'),
    path('category/<str:cat_name>',blogView,name='category'),
    path('tag/<str:tag_name>',blogView,name='tag'),
    path('author/<str:author_uname>',blogView,name='author'),
    path('search/?s',blogSearch,name='search'),
]