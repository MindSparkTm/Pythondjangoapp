from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()

router.register(r'useradapi', api.Useradviewset)








urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^index/$', views.Index.as_view(), name='Index'),


    url(r'^menseekingwomen/$', views.Menseekingwomen.as_view(), name='Menseekingwomen'),
    url(r'^menseekingmen/$', views.Menseekingmen.as_view(), name='Menseekingmen'),
    url(r'^womenseekingmen/$', views.Womenseekingmen.as_view(), name='Womenseekingmen'),
    url(r'^womenseekingwomen/$', views.Womenseekingwomen.as_view(), name='Womenseekingwomen'),
    url(r'^menseekingmen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),
    url(r'^menseekingwomen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),
    url(r'^womenseekingmen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),
    url(r'^womenseekingwomen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),

    url(r'^getdatafromad/$', views.getdatafromad, name='getdatafromad'),
    url(r'^replyadpost/$', views.replyforad, name='replyforad'),

)



