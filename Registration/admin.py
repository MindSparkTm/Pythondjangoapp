from django.contrib import admin
from django import forms
from .models import Users


# Register your models here.




class Userinfo(admin.ModelAdmin):

    list_display = ['user_id','created', 'name','phone', 'email','age',]
admin.site.register(Users, Userinfo)


