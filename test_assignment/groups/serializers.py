from rest_framework import serializers
from .heromodel import Hero

class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = '__all__'


