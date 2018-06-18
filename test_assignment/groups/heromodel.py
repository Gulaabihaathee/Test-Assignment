from django.db import models
from datetime import datetime
from .groupmodel import Group


class Hero(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True)
    wins_counter = models.PositiveIntegerField(default=0)
    defeats_counter = models.PositiveIntegerField(default=0)
    is_killed = models.BooleanField(default=False)
    murder_date = models.DateTimeField(null=True, blank=True)
    defeat_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def win(self):
        self.wins_counter += 1
        self.save()

    def loss(self):
        self.defeats_counter += 1
        self.defeat_date = datetime.now()
        self.save()

    def kill(self):
        self.is_killed = True
        self.murder_date = datetime.now()
        self.save()
