from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('index/', views.Index.as_view(), name='index'),
    url('logout/', views.Logout.as_view(), name='logout')

]
