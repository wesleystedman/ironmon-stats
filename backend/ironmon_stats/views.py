from rest_framework import generics
from rest_framework import permissions
from .models import Run, Pokemon
from django.contrib.auth.models import User
from .serializers import RunSerializer, PokemonSerializer, UserSerializer
from .permissions import IsRunOwnerOrReadOnly, IsPokemonOwnerOrReadOnly


class RunList(generics.ListCreateAPIView):
  queryset =  Run.objects.all()
  serializer_class = RunSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsRunOwnerOrReadOnly]


class RunDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Run.objects.all()
  serializer_class = RunSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsRunOwnerOrReadOnly]


class PokemonList(generics.ListCreateAPIView):
  queryset =  Pokemon.objects.all()
  serializer_class = PokemonSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPokemonOwnerOrReadOnly]


class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPokemonOwnerOrReadOnly]


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
