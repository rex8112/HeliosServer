from rest_framework import serializers

from .models import Server, Channel, Member, Stadium, Race, Horse


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'server', 'type', 'settings', 'flags']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'server', 'member_id', 'settings', 'flags']


class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class StadiumSerializer(serializers.ModelSerializer):
    horses = HorseSerializer(many=True, required=False, read_only=True)
    races = RaceSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Stadium
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, required=False, read_only=True)
    members = MemberSerializer(many=True, required=False, read_only=True)
    stadium = StadiumSerializer(required=False, read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'name', 'settings', 'flags', 'channels', 'members', 'stadium']
