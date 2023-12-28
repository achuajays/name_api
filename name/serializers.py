from rest_framework import serializers
from .models import name
class nameserl(serializers.ModelSerializer):
    class Meta:
        model = name 
        fields = '__all__'

