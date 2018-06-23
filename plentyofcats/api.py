from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters




class Useradviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Userad.objects.all()
    serializer_class = serializers.useradserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','category','country')


class Replyadviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Replyad.objects.all()
    serializer_class = serializers.replyadserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','email')










