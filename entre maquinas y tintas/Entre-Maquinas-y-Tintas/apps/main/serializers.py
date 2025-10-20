from rest_framework import serializers
from .models import Machine, Ink

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'description', 'created_at']

class InkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ink
        fields = ['id', 'color', 'type', 'created_at']