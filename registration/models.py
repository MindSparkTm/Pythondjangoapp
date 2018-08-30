from django.db import models
from django.utils import timezone


# Create your models here.


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    gymname = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    contactperson = models.CharField(max_length=100)
    blog = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    paybill = models.CharField(max_length=100, null=True, blank=True)
    paymentcontactnumber = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('last_updated',)

    def __str__(self):
        return "%s %s" % (self.id, self.gymname)
