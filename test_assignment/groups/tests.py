from django.test import TestCase
from .heromodel import Hero
from .groupmodel import Group
from .pairingmodel import PairingModel
from random import randint

class ProjectTestCases(TestCase):
    def setUp(self):
        Hero.objects.create(name='Test Hero', is_killed=False)
        Group.objects.create(name='Testers')

        for i in range(randint(4,10)):
            Hero.objects.create(name=str(i), group=Group.objects.get(name='Testers'))

        PairingModel.objects.create(group_name='Testers')

    def test_kill(self):
        test_hero = Hero.objects.get(name='Test Hero')
        test_hero.kill()
        self.assertEqual(test_hero.is_killed, True)

    def test_pairing(self):
        # String with all possible pairs with no repetition
        all_pairing_possibilities = ''
        pairing_string = ''
        # Number of all possible pairs with no repetition
        sum_of_combinations = 0

        # Number of heroes in testers group
        all_testers = Hero.objects.filter(group=Group.objects.get(name='Testers')).count()

        # Calculating Number of all possible pairs with no repetition
        for i in range(all_testers):
            sum_of_combinations += i

        PairingModel.objects.get(group_name='Testers').make_interaction_array()

        while True:
            if pairing_string == 'Heroes cannot be paired, make array.':
                break

            PairingModel.objects.get(group_name='Testers').Pairing()
            pairing_string = PairingModel.objects.get(group_name='Testers').pairs
            all_pairing_possibilities += pairing_string

        possibilites_counter = all_pairing_possibilities.split('\n')
        self.assertEqual(len(possibilites_counter), sum_of_combinations+1)
