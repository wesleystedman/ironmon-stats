from rest_framework import serializers
from .models import Run

class RunSerializer(serializers.ModelSerializer):

  class Meta:
    model = Run
    fields = ('pk', 'game', 'attempt', 'endpoint', 'settings_string', 'run_seed', 'randomizer_version', 'notes', 'user')
