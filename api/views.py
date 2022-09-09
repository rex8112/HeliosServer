import datetime

from rest_framework import viewsets, permissions

from .models import (Server, Channel, Member, Stadium, Race, Horse, Record,
                     Auction)
from .serializers import (ServerSerializer, ChannelSerializer,
                          MemberSerializer, StadiumSerializer, RaceSerializer,
                          HorseSerializer, RecordSerializer, AuctionSerializer)


# Create your views here.
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticated]


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.IsAuthenticated]


class HorseViewSet(viewsets.ModelViewSet):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on server parameter."""
        queryset = Horse.objects.all()
        server_id = self.request.query_params.get('server')
        if server_id is not None:
            queryset = queryset.filter(server__server__id=server_id)

        return queryset


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on server parameter."""
        queryset = Race.objects.all()
        server_id = self.request.query_params.get('server')
        if server_id is not None:
            queryset = queryset.filter(server__server__id=server_id)

        return queryset


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on parameters"""
        queryset = Record.objects.all()
        horse_id = self.request.query_params.get('horse')
        allow_basic = self.request.query_params.get('basic')
        after = self.request.query_params.get('after')
        if horse_id is not None:
            queryset = queryset.filter(horse=horse_id)
        if allow_basic is None:
            queryset = queryset.exclude(type='basic')
        if after is not None:
            after = datetime.datetime.fromisoformat(after).date()
            queryset = queryset.filter(date__gt=after)
        return queryset


class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on server parameter."""
        queryset = Auction.objects.all()
        server_id = self.request.query_params.get('server')
        if server_id is not None:
            queryset = queryset.filter(server__id=server_id)

        return queryset


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on server parameter."""
        queryset = Channel.objects.all()
        server_id = self.request.query_params.get('server')
        type_param = self.request.query_params.get('type')
        if server_id is not None:
            queryset = queryset.filter(server__id=server_id)
        if type_param is not None:
            queryset = queryset.filter(type=type_param)

        return queryset


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter based on parameters"""
        queryset = Member.objects.all()
        server_id = self.request.query_params.get('server')
        member_id = self.request.query_params.get('member_id')
        if server_id is not None:
            queryset = queryset.filter(server__id=server_id)
        if member_id is not None:
            queryset = queryset.filter(member_id=member_id)

        return queryset
