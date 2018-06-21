from . import models

from rest_framework import serializers







class useradserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Userad
        fields = ('user_id', 'created', 'title','description','age','country','category')






