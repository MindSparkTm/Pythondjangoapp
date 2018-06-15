from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()

router.register(r'registerservice', api.RegisterUserService)








urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^register/$', views.RegisterUsers.as_view(), name='RegisterUsers'),

)

