from .models import Server, Channel
from rest_framework import serializers


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'server', 'type']


class ServerSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'name', 'settings', 'flags', 'channels']
