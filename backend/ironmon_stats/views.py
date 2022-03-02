from rest_framework import generics
from rest_framework import permissions
from .models import Run, Pokemon
from django.contrib.auth.models import User
from .serializers import RunSerializer, PokemonSerializer, UserSerializer

class IsRunOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user


class IsPokemonOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.run_instance.user == request.user


class RunList(generics.ListCreateAPIView):
  queryset =  Run.objects.all()
  serializer_class = RunSerializer
  permission_classes = [IsRunOwnerOrReadOnly]


class RunDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Run.objects.all()
  serializer_class = RunSerializer
  permission_classes = [IsRunOwnerOrReadOnly]


class PokemonList(generics.ListCreateAPIView):
  queryset =  Pokemon.objects.all()
  serializer_class = PokemonSerializer
  permission_classes = [IsPokemonOwnerOrReadOnly]


class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer
  permission_classes = [IsPokemonOwnerOrReadOnly]


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
