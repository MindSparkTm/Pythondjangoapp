from django.contrib import admin
from django import forms
from .models import Userad,Replyad,Usads,Europeads


# Register your models here.




class Useradinfo(admin.ModelAdmin):

    list_display = ['postid','created', 'uploaded_file','category','title','description', 'email','country','age','uploaded_file_url']

admin.site.register(Userad, Useradinfo)


class Usaadinfo(admin.ModelAdmin):

    list_display = ['postid','created', 'uploaded_file','category','title','description', 'email','state','age','uploaded_file_url']

admin.site.register(Usads, Usaadinfo)


class Europeadinfo(admin.ModelAdmin):

    list_display = ['postid','created', 'uploaded_file','category','title','description', 'email','country','state','age','uploaded_file_url']

admin.site.register(Europeads, Europeadinfo)

class Replyadinfo(admin.ModelAdmin):
        list_display = ['postid', 'created', 'uploaded_file', 'description', 'email',
                         'uploaded_file_url']

admin.site.register(Replyad, Replyadinfo)






