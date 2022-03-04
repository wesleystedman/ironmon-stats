from rest_framework import permissions, viewsets
from .models import Run, Pokemon
from django.contrib.auth.models import User
from .serializers import RunSerializer, PokemonSerializer, UserSerializer
from .permissions import IsRunOwnerOrReadOnly, IsPokemonOwnerOrReadOnly


class RunViewSet(viewsets.ModelViewSet):
  queryset =  Run.objects.all()
  serializer_class = RunSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsRunOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class PokemonViewSet(viewsets.ModelViewSet):
  queryset =  Pokemon.objects.all()
  serializer_class = PokemonSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPokemonOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
