from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()









urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^index/$', views.Index.as_view(), name='Index'),

)



