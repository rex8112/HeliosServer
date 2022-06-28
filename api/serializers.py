from .models import Server, Channel
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    channels = serializers.ManyRelatedField()

    class Meta:
        model = Server
        fields = ['id', 'name', 'settings', 'flags', 'channels']


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'server', 'type']
