from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.core.signing import Signer



class Index(CreateView):

    def get(self, request):
        return render(request, 'accounts/index.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            uname = request.POST['username']
            print ('uname',uname)

            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])

            if user is not None:
                login(request, user)

                uname = user.username
                print('email',uname)


                return redirect(reverse('registration:register',kwargs={"uname":uname}))
            else:
                return render(request, "accounts/index.html")





class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('index'))
