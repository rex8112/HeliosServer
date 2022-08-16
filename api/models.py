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
    id = models.AutoField(primary_key=True)
    server = models.ForeignKey(Server, related_name='members', on_delete=models.CASCADE)
    member_id = models.BigIntegerField()
    templates = models.JSONField(default=list)
    settings = models.JSONField(default=dict)
    flags = models.JSONField(default=list)


class Stadium(models.Model):
    server = models.OneToOneField(Server, related_name='stadium', on_delete=models.CASCADE, primary_key=True)
    day = models.IntegerField(default=0)
    settings = models.JSONField(default=dict)
    events = models.JSONField(default=list)


class Horse(models.Model):
    id = models.AutoField(primary_key=True)
    server = models.ForeignKey(Stadium, related_name='horses', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    stats = models.JSONField(default=dict)
    born = models.JSONField(default=tuple)
    settings = models.JSONField(default=dict)
    flags = models.JSONField(default=list)


class Race(models.Model):
    id = models.AutoField(primary_key=True)
    server = models.ForeignKey(Stadium, related_name='races', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    horses = models.JSONField(default=list)
    bets = models.JSONField(default=list)
    settings = models.JSONField(default=dict)


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    horse = models.ForeignKey(Horse, related_name='records', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='records', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    earnings = models.BigIntegerField(default=0)
    placing = models.IntegerField()
    date = models.DateField()


