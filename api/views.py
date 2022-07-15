from rest_framework import viewsets, permissions

from .models import Server, Channel, Member
from .serializers import ServerSerializer, ChannelSerializer, MemberSerializer


# Create your views here.
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticated]


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
