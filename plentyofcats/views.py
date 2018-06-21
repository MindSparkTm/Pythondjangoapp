from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Userad
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


import logging



class Index(CreateView):

    model = Userad

    def get(self, request):
        return render(request, 'plentyofcats/index.html')


    def post(self,request):

        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        age = int(request.POST['age'])
        country = request.POST['country']
        email = request.POST['email']
        uploadedfile= request.FILES['uploadedfile']
        fs = FileSystemStorage()

        filename = fs.save(uploadedfile.name, uploadedfile)
        uploaded_file_url = fs.url(filename)


        userad = Userad(title=title,email=email,description=description,category=category,age=age,country=country,uploaded_file_url=uploaded_file_url)
        userad.save()

        return HttpResponseRedirect(reverse("Index"))





class Menseekingwomen(CreateView):

    model = Userad

    def get(self, request):


        return render(request, 'plentyofcats/menseekingwomen.html')

def getdatafromad(request):
    if request.method == 'GET':
        category = request.GET['category']
        country = request.GET['country']
        userad = Userad.objects.filter(category=category).filter(country=country).values()
        userad = list(userad)
        print('userad',userad)





        return JsonResponse(userad,safe=False)  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")




