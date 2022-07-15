from rest_framework import serializers

from .models import Server, Channel, Member


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'server', 'type', 'settings', 'flags']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'server', 'member_id', 'settings', 'flags']


class ServerSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, required=False, read_only=True)
    members = MemberSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'name', 'settings', 'flags', 'channels', 'members']
