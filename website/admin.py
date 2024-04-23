from django.contrib import admin
from website.models import *
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass



# در فایل models.py
from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


