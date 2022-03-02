from rest_framework import generics

from .models import Run, Pokemon
from .serializers import RunSerializer, PokemonSerializer

class RunList(generics.ListCreateAPIView):
  queryset =  Run.objects.all()
  serializer_class = RunSerializer


class RunDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Run.objects.all()
  serializer_class = RunSerializer
