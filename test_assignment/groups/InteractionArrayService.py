import os.path
import pickle
import numpy as np


def make_interaction_array(size):
    # size = Hero.objects.count()+1
    InteractionMatrix = np.triu(np.ones((size, size)).astype(np.int), 1)
    DumpInteractionArray(InteractionMatrix)


def LoadInteractionArray():
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'rb') as file:
        InteractionMatrix = pickle.load(file)
    return InteractionMatrix


def DumpInteractionArray(InteractionMatrix):
    with open(os.path.dirname(__file__)+'/../interaction_array.pickle', 'wb') as file:
        pickle.dump(InteractionMatrix, file)