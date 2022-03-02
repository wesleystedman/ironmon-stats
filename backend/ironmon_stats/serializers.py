from rest_framework import serializers
from .models import Pokemon, Run

class PokemonSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pokemon
    fields = '__all__'


class RunSerializer(serializers.ModelSerializer):
  pokemons = serializers.PrimaryKeyRelatedField(many=True, queryset=Pokemon.objects.all())

  class Meta:
    model = Run
    fields = ['pk', 'game', 'attempt', 'endpoint', 'settings_string', 'run_seed', 'randomizer_version', 'notes', 'user', 'pokemons']
