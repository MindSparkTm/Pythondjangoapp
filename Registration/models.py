from django.db import models
from django.utils import timezone


# Create your models here.






class Users(models.Model):

    user_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)


class Testdata(models.Model):
    Id = models.AutoField(primary_key=True)
    Series_reference = models.CharField(max_length=1000, null=True, blank=True)
    Period = models.CharField(max_length=1000, null=True, blank=True)
    Data_value = models.CharField(max_length=1000, null=True, blank=True)
    STATUS = models.CharField(max_length=1000, null=True, blank=True)
    UNITS = models.CharField(max_length=1000, null=True, blank=True)
    Subject = models.CharField(max_length=1000, null=True, blank=True)
    Group = models.CharField(max_length=1000, null=True, blank=True)
    Series_title_1 = models.CharField(max_length=1000, null=True, blank=True)



