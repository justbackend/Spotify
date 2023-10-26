from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_davomiylik(self, value):
        if int(value) > 300:
            raise serializers.ValidationError("fda;ljsk")
        return value

    def validate_nom(self, value):
        if value[-5:-1] != ".mp3":
            raise serializers.ValidationError('fsal;')
        return value

class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = "__all__"



class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"