from . import models

from rest_framework import serializers







class registerbillserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = '__all__'




class testdataserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Testdata
        fields = '__all__'



