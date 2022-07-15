from rest_framework import serializers

from .models import Server, Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'server', 'type', 'settings', 'flags']


class ServerSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'name', 'settings', 'flags', 'channels']
