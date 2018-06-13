import os.path
import pickle
import numpy as np
from .heromodel import Hero

def make_interaction_array():
    N = Hero.objects.count()+1
    InteractionMatrix = np.triu(np.ones((N, N)).astype(np.int), 1)

    with open('interaction_array.pickle', 'wb') as file:
        pickle.dump(InteractionMatrix, file)


def OpenLoadInteractionMatrix():
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'rb') as file:
        InteractionMatrix = pickle.load(file)
    return InteractionMatrix

def OpenDumpInteractionMatrix(InteractionMatrix):
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'wb') as file:
        pickle.dump(InteractionMatrix, file)