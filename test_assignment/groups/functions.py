from .heromodel import Hero
import datetime
from random import choice
import pickle
import numpy as np
import os.path


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
    InteractionMatrix = np.triu(np.ones((N, N)).astype(np.int), 1)

    with open('interaction_array.pickle', 'wb') as file:
        pickle.dump(InteractionMatrix, file)


def Pairing(group_id):
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'rb') as file:
        InteractionMatrix = pickle.load(file)

    heroes = Hero.objects.filter(defeat_date__isnull = True).filter(is_killed=False).filter(group=group_id)
    indexes = list(map(lambda x: x.id, heroes))

    pairs = []

    while len(pairs) != len(heroes)//2:
        PossiblePairs = 0

        for i in range(len(indexes) - 1):
            for j in range(i + 1, len(indexes)):
                PossiblePairs += InteractionMatrix[indexes[i], indexes[j]]

        if PossiblePairs == 0:
            break

        set1 = set(indexes)
        chosen1 = choice(indexes)
        set2 = set1 - set([chosen1])
        chosen2 = choice(list(set2))

        if InteractionMatrix[chosen1, chosen2] == 1:
            pairs.append([Hero.objects.filter(id=chosen1), Hero.objects.filter(id=chosen2)])
            InteractionMatrix[chosen1, chosen2] = 0

    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'wb') as file:
        pickle.dump(InteractionMatrix, file)

    return pairs