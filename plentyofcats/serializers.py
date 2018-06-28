from . import models

from rest_framework import serializers







class useradserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Userad
        fields = ('postid', 'created', 'title','description','age','country','category')

class usaadserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Userad
        fields = ('postid', 'created', 'title','description','age','state','category')


class europeadserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Userad
        fields = ('postid', 'created', 'title','description','age','country','state','category')


class replyadserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Replyad
        fields = ('postid', 'created','description','email')





