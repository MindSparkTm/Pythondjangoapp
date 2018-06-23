from django.db import models
from django.utils import timezone


# Create your models here.






class Userad(models.Model):

    postid = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=10000, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    category = models.CharField(max_length=30,null=True, blank=True)
    country = models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    uploaded_file = models.FileField(upload_to='media/users/', null=True, blank=True)
    uploaded_file_url = models.CharField(max_length=30,null=True,blank=True)





class Replyad(models.Model):

    postid = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=10000, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)

    uploaded_file = models.FileField(upload_to='media/users/', null=True, blank=True)
    uploaded_file_url = models.CharField(max_length=30,null=True,blank=True)









