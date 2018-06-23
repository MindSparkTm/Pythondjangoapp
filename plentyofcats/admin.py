from django.contrib import admin
from django import forms
from .models import Userad,Replyad


# Register your models here.




class Useradinfo(admin.ModelAdmin):

    list_display = ['postid','created', 'uploaded_file','category','title','description', 'email','country','age','uploaded_file_url']

admin.site.register(Userad, Useradinfo)


class Replyadinfo(admin.ModelAdmin):
        list_display = ['postid', 'created', 'uploaded_file', 'description', 'email',
                         'uploaded_file_url']

admin.site.register(Replyad, Replyadinfo)






