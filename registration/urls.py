from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('register/', views.RegistrationCreateView.as_view(), name='register')
]
