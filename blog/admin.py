from django.contrib import admin
from blog.models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title','author','id','status','counted_view','published_date',)
    # ordering = ('status','-counted_view','published_date',)
    search_fields = ('title','content',)
    summernote_fields = ('content',)
# admin.site.register(Post,PostAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','post','created_date','approved')
    # ordering = ('status','-counted_view','published_date',)
    search_fields = ('post','name')

admin.site.register(Comment,CommentAdmin)