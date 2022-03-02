from rest_framework import serializers
from .models import Pokemon, Run

class PokemonSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pokemon
    fields = '__all__'


class RunSerializer(serializers.ModelSerializer):
  pokemon = PokemonSerializer(required=False, many=True)

  class Meta:
    model = Run
    fields = '__all__'
