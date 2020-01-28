"""
channels/serializers.py
"""
from rest_framework import serializers
from channels.models import Channels


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ('id', 'title', 'description')
