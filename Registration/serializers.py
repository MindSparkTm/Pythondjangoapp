from . import models

from rest_framework import serializers







class registerbillserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = '__all__'




