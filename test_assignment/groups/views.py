from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .heromodel import Hero
from .serializers import HeroSerializer


def ranking(request):
    heroes = Hero.objects.filter(is_killed=False).order_by('-wins_counter', 'defeats_counter')
    ranking_string = ''

    for hero in heroes:
        ranking_string += str(hero.wins_counter) + ' ' + str(hero.defeats_counter) + ' ' + str(hero.name) + '<br>'

    return HttpResponse(ranking_string)


class HeroRanking(APIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request):
        heroes = Hero.objects.filter(is_killed=False).order_by('-wins_counter', 'defeats_counter')
        HeroSerializer.Meta.fields = ('name', 'wins_counter', 'defeats_counter')
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)

class DefeatedHeroList(APIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request):
        heroes = Hero.objects.filter(defeat_date__isnull = False).order_by('-wins_counter')
        HeroSerializer.Meta.fields = ('name', 'wins_counter', 'defeat_date')
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)
