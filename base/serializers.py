from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSetting
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
