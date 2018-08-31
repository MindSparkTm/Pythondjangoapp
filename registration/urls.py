from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('currentuser/(?P<uname>\w+)', views.RegistrationCreateView.as_view(), name='register'),
    url('newuser/', views.FirsttimeuserCreateView.as_view(), name='newuser')

]
