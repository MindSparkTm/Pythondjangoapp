from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Registration
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


class RegistrationCreateView(CreateView):
    model = Registration

    def get(self, request, uname, *args, **kwargs):

        registration = Registration.objects.filter(username=uname).values()
        print('uname',uname)
        self.request.session['_uname'] = uname


        if not registration:
            print('entered')
            return redirect('registration:newuser')

        else:
            return render(request, 'registration/registerform.html', {'record': registration})

    def post(self, request):
        gymname = request.POST['gymname']
        email = request.POST['email']
        mobilenumber = request.POST['phonenumber']
        country = request.POST['country']
        country = country.lower()
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


class FirsttimeuserCreateView(CreateView):
    def get(self, request):
        uname = self.request.session['_uname']
        return render(request, 'registration/newuser.html', {'rec': uname})
