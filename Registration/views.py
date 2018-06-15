from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Users,Testdata
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd

import logging



class RegisterUsers(CreateView):

    model = Users

    def get(self, request):
        return render(request, 'Registration/registerform.html')

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





                fileinfo = pd.read_csv(csv_file,sep=',',names=['Series_reference','Period', 'Data_value','STATUS', 'UNITS','Subject','Group','Series_title_1','Series_title_2','Series_title_3','Series_tile_4','Series_tile_5'],skiprows=1)
                #serie = fileinfo[fileinfo['Series_reference']]
                s = fileinfo['Series_reference'].values.tolist()
                p = fileinfo['Period'].values.tolist()
                d = fileinfo['Data_value'].values.tolist()
                st =fileinfo['STATUS'].values.tolist()
                u= fileinfo['UNITS'].values.tolist()
                sub = fileinfo['Subject'].values.tolist()
                gr = fileinfo['Group'].values.tolist()
                stt= fileinfo['Series_title_1'].values.tolist()

                instances = [
                         Testdata(Series_reference=s[pos], Period=p[pos], Data_value=d[pos], STATUS=st[pos],
                                                            UNITS= u[pos],Subject=sub[pos],Group=gr[pos],Series_title_1=stt[pos])
                    for pos, item in enumerate(s)

                    ]

                Testdata.objects.bulk_create(instances)











                messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
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

