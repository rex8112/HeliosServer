from django.db import models


# Create your models here.
class Server(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    settings = models.JSONField()
    flags = models.JSONField()


class Channel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    server = models.ForeignKey(Server, related_name='channels', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    settings = models.JSONField(default=dict)
    flags = models.JSONField(default=list)


class Member(models.Model):
    id = models.BigIntegerField(primary_key=True)
    server = models.ForeignKey(Server, related_name='members', on_delete=models.CASCADE)
    member_id = models.BigIntegerField()
    settings = models.JSONField(default=dict)
    flags = models.JSONField(default=list)
