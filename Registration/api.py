from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters




class RegisterUserService(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Users.objects.all()
    serializer_class = serializers.registerbillserializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_id',)








