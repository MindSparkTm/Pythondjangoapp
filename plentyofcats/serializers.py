from . import models

from rest_framework import serializers







class useradserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Userad
        fields = ('postid', 'created', 'title','description','age','country','category')


class replyadserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Replyad
        fields = ('postid', 'created','description','email')





