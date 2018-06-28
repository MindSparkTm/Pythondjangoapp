from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters




class Useradviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Userad.objects.all()
    serializer_class = serializers.useradserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','category','country')



class Usaadviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Usads.objects.all()
    serializer_class = serializers.usaadserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','category','state')


class Europeadviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Europeads.objects.all()
    serializer_class = serializers.europeadserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','category','country','state')


class Replyadviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Replyad.objects.all()
    serializer_class = serializers.replyadserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('postid','email')










