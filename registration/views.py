from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Registration
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

import sendgrid
import os
from sendgrid.helpers.mail import *
import base64

import logging


class RegistrationCreateView(CreateView):
    model = Registration

    def get(self, request):
        return render(request, 'registration/registerform.html')

    def post(self, request):
        gymname = request.POST['gymname']
        email = request.POST['email']
        mobilenumber = request.POST['phonenumber']
        country = request.POST['country']
        country= country.lower()
        state = request.POST['state']
        state = state.lower()
        zipcode = request.POST['zipcode']
        address = request.POST['address']
        paybillnumber = request.POST['paybillnumber']
        paymentnumber = request.POST['paymentnumber']
        blog = request.POST['blog']
        website = request.POST['website']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']

        registration = Registration(gymname=gymname, email=email, phonenumber=mobilenumber,
                                    country=country, state=state, zipcode=zipcode, location=address,
                                    paybill=paybillnumber, paymentcontactnumber=paymentnumber, blog=blog,
                                    website=website, facebook=facebook, instagram=instagram)
        registration.save()

        return HttpResponseRedirect(reverse("register"))
