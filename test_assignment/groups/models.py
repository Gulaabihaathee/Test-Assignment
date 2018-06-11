from django.db import models
import datetime
from random import choice
import pickle
import numpy as np
import os.path

class Group(models.Model):
    group_name = models.CharField(max_length=250)

    def __str__(self):
        return self.group_name


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


def kill(Hero):
    Hero.is_killed = True
    Hero.murder_date = datetime.datetime.now()
    Hero.save()


def win(Hero):
    Hero.wins_counter += 1
    Hero.save()


def loss(Hero):
    Hero.defeats_counter += 1
    Hero.defeat_date = datetime.datetime.now()
    Hero.save()


def make_interaction_array():
    N = Hero.objects.count()+1
    IA = np.triu(np.ones((N, N)).astype(np.int), 1)

    with open('interaction_array.pickle', 'wb') as f:
        pickle.dump(IA, f)

def Pairing(group_id):
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'rb') as f:
        IA = pickle.load(f)

    heroes = Hero.objects.filter(defeat_date__isnull = True).filter(group=group_id)
    indexes = list(map(lambda x: x.id, heroes))

    pairs = []
    p = 1

    while len(pairs)!= len(heroes)//2:
        p = 0
        for i in range(len(indexes) - 1):
            for j in range(i + 1, len(indexes)):
                p += IA[indexes[i], indexes[j]]
        if p==0:
            break
        set1 = set(indexes)
        chosen1 = choice(indexes)
        set2 = set1 - set([chosen1])
        chosen2 = choice(list(set2))
        if IA[chosen1, chosen2] == 1:
            pairs.append([Hero.objects.filter(id=chosen1), Hero.objects.filter(id=chosen2)])
            IA[chosen1, chosen2] = 0

    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'wb') as f:
        pickle.dump(IA, f)

    return pairs


