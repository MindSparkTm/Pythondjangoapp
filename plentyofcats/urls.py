from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()

router.register(r'useradapi', api.Useradviewset)

router.register(r'usaadapi', api.Usaadviewset)







urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^index/$', views.Index.as_view(), name='Index'),
    url(r'^usa/$', views.Usaindex.as_view(), name='Usaindex'),

    url(r'^menseekingwomen/$', views.Menseekingwomen.as_view(), name='Menseekingwomen'),
    url(r'^menseekingwomenus/$', views.Menseekingwomenus.as_view(), name='Menseekingwomenus'),

    url(r'^menseekingmen/$', views.Menseekingmen.as_view(), name='Menseekingmen'),
    url(r'^menseekingmenus/$', views.Menseekingmenus.as_view(), name='Menseekingmenus'),

    url(r'^womenseekingmen/$', views.Womenseekingmen.as_view(), name='Womenseekingmen'),
    url(r'^womenseekingmenus/$', views.Womenseekingmenus.as_view(), name='Womenseekingmenus'),

    url(r'^womenseekingwomen/$', views.Womenseekingwomen.as_view(), name='Womenseekingwomen'),
    url(r'^womenseekingwomenus/$', views.Womenseekingwomenus.as_view(), name='Womenseekingwomenus'),

    url(r'^menseekingmen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),

    url(r'^menseekingmenus/displaypost/(?P<id>\S+)/$', views.Uspostdetails.as_view(), name='Uspostdetails'),
    url(r'^menseekingwomenus/displaypost/(?P<id>\S+)/$', views.Uspostdetails.as_view(), name='Uspostdetails'),
    url(r'^womenseekingmenus/displaypost/(?P<id>\S+)/$', views.Uspostdetails.as_view(), name='Uspostdetails'),
    url(r'^womenseekingwomenus/displaypost/(?P<id>\S+)/$', views.Uspostdetails.as_view(), name='Uspostdetails'),

    url(r'^menseekingwomen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),
    url(r'^womenseekingmen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),
    url(r'^womenseekingwomen/displaypost/(?P<id>\S+)/$', views.Postdetails.as_view(), name='Postdetails'),

    url(r'^getdatafromad/$', views.getdatafromad, name='getdatafromad'),
    url(r'^getdatafromusad/$', views.getdatafromusad, name='getdatafromusad'),

    url(r'^replyadpost/$', views.replyforad, name='replyforad'),

)



