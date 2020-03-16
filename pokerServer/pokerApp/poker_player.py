from django.db import models


class PokerPlayer(models.Model):
    name = models.CharField(max_length=30)
    stack = models.IntegerField()
