from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Users
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd

import logging



class RegisterUsers(CreateView):

    model = Users

    def get(self, request):
        return render(request, 'busararegistration/registerform.html')

    def post(self, request):
        count =0

        print('Entered 1')
        seen = set()

        try:
            csv_file = request.FILES["csv_file"]
            print('csv',csv_file)
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("RegisterUsers"))

            # if file is too large, return
            if csv_file.multiple_chunks():





                fileinfo = pd.read_csv(csv_file,sep=',',names=['name','phone', 'email','age'],skiprows=1)
                fileinfo_clean = fileinfo.drop_duplicates(subset=['name', 'phone','email','age'])

                Name = fileinfo_clean['name'].values.tolist()
                Phone = fileinfo_clean['phone'].values.tolist()
                Email = fileinfo_clean['email'].values.tolist()
                Age = fileinfo_clean['age'].values.tolist()


                instances = [


                         Users(name=Name[pos], phone=Phone[pos], email=Email[pos], age=Age[pos])
                    for pos, item in enumerate(Name)

                    ]

                Users.objects.bulk_create(instances)











                #messages.error(request, "Uploaded file (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                return HttpResponseRedirect(reverse("RegisterUsers"))
            else:
                 file_data = csv_file.read().decode("utf-8")
                 print('Entered 2')
                 lines = file_data.split("\n")
                 for line in lines:
                     if line:
                         print('Entered 3')
                         count=count+1
                         print('count',count)
                         if count>=2:
                             if line in seen:continue
                             seen.add(line)
                             fields = line.split(",")
                             name = fields[0]
                             phone = fields[1]
                             email = fields[2]
                             age = fields[3]
                             print(name,phone,email,age)
                             try:
                                 print('Entered')
                                 b = Users(name=name,phone=phone,email=email,age=age)
                                 b.save()
                             except Exception as e:
                                     logging.getLogger("error_logger").error(repr(e))
                             pass

        except Exception as e:
            logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
            messages.error(request, "Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("RegisterUsers"))

class DisplayUsers(CreateView):
    def get(self, request):
        return render(request, 'busararegistration/viewusers.html')




