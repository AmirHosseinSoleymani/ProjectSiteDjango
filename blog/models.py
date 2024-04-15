from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=111)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/',default='def.jpg')
    tags = TaggableManager()
    category = models.ManyToManyField(Category) #default can be null
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) #or CASECADE  
    
    class Meta:
        ordering = ['created_date']



    def __str__(self) -> str:
        return f" {self.title}  [{self.id}]" 
    
    

    def get_absolute_url(self):
        return reverse("blog:blog-single", kwargs={'id':self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name