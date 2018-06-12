from django.db import models
from .groupmodel import Group


class Hero(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    hero_name = models.CharField(max_length=250)
    wins_counter = models.PositiveIntegerField(default=0)
    defeats_counter = models.PositiveIntegerField(default=0)
    is_killed = models.BooleanField(default=False)
    murder_date = models.DateTimeField(null=True, blank=True)
    defeat_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.hero_name






