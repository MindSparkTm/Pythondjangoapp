from django.contrib import admin
from django import forms
from .models import Userad


# Register your models here.




class Useradinfo(admin.ModelAdmin):

    list_display = ['user_id','created', 'uploaded_file','category','title','description', 'email','country','age','uploaded_file_url']
admin.site.register(Userad, Useradinfo)


