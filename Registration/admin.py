from django.contrib import admin
from django import forms
from .models import Users,Testdata


# Register your models here.




class Userinfo(admin.ModelAdmin):

    list_display = ['user_id','created', 'name','phone', 'email','age',]
admin.site.register(Users, Userinfo)


class Testinfo(admin.ModelAdmin):

    list_display = ['Id','Series_reference','Period', 'Data_value','STATUS', 'UNITS','Subject','Group','Series_title_1']
admin.site.register(Testdata, Testinfo)