from django.db import models
from numpy import triu, ravel, reshape, fromstring, array2string, ones, arange
from random import choice
from .heromodel import Hero
from .groupmodel import Group

class PairingModel(models.Model):
    interaction_array = models.CharField(max_length=10000, blank=True)
    group_name = models.CharField(max_length=250, null=True, blank=True)
    pairs = models.TextField(max_length=10000, null=True, blank=True)


    def make_interaction_array(self):
        N = Hero.objects.filter(group=Group.objects.get(name=self.group_name)).count()+1
        array = triu(ones((N, N)), 1).astype(int)
        string_array = array2string(ravel(array))[1:-1]
        self.interaction_array = string_array
        self.save()



    def Pairing(self):
        try:
            group_id = Group.objects.filter(name=self.group_name)[0].id
        except IndexError:
            self.pairs = 'This group does not exist or does not have enough heroes to pair.'
            self.save()
        else:
            N = Hero.objects.filter(group=Group.objects.get(name=self.group_name)).count() + 1
            InteractionMatrix = reshape(fromstring(self.interaction_array, dtype=int, sep=' '), (N, N))

            heroes = Hero.objects.filter(defeat_date__isnull=True).filter(is_killed=False).filter(group=group_id)
            indexes1 = list(map(lambda x: x.id, heroes))
            mapping_indexes = arange(len(indexes1))

            pairs = []

            while len(pairs) != len(heroes) // 2:
                PossiblePairs = 0

                for i in range(len(mapping_indexes) - 1):
                    for j in range(i + 1, len(mapping_indexes)):
                        PossiblePairs += InteractionMatrix[mapping_indexes[i], mapping_indexes[j]]

                if PossiblePairs == 0:
                    break

                set1 = set(mapping_indexes)
                chosen1 = choice(mapping_indexes)
                set2 = set1 - set([chosen1])
                chosen2 = choice(list(set2))

                if InteractionMatrix[chosen1, chosen2] == 1:
                    pairs.append([Hero.objects.filter(id=indexes1[chosen1]), Hero.objects.filter(id=indexes1[chosen2])])
                    InteractionMatrix[chosen1, chosen2] = 0

            array = InteractionMatrix
            string_array = array2string(ravel(array))[1:-1]
            self.interaction_array = string_array

            pairs_string = ''
            if pairs == []:
                self.pairs = 'Heroes cannot be paired, make array.'
            else:
                for pair in pairs:
                    pairs_string += ' - '.join(list(map(lambda x: x[0].name, pair))) + '\n'
                self.pairs = pairs_string

            self.save()



    def __str__(self):
        return self.group_name
