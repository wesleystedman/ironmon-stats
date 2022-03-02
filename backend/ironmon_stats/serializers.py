from rest_framework import serializers
from .models import Pokemon, Run
from django.contrib.auth.models import User

class PokemonSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pokemon
    fields = '__all__'


class RunSerializer(serializers.ModelSerializer):
  pokemon = serializers.PrimaryKeyRelatedField(many=True, queryset=Pokemon.objects.all())
  user = serializers.ReadOnlyField(source='user.username')

  class Meta:
    model = Run
    fields = ['pk', 'game', 'attempt', 'endpoint', 'settings_string', 'run_seed', 'randomizer_version', 'notes', 'user', 'pokemon']


class UserSerializer(serializers.ModelSerializer):
  runs = serializers.PrimaryKeyRelatedField(many=True, queryset=Run.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'runs']
