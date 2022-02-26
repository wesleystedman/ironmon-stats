from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Run(models.Model):
  game = models.CharField(max_length=14) # pokeapi version name, enforced by client
  attempt = models.PositiveIntegerField() # unique with game and user? auto-increment?
  endpoint = models.CharField(max_length=100, blank=True) # client suggestions/enforcement?
  settings_string = models.CharField(max_length=100, blank=True) # TODO: check actual max size
  run_seed = models.CharField(max_length=100, blank=True) # TODO: check actual max size
  randomizer_version = models.CharField(max_length=20, blank=True)
  notes = models.TextField(max_length=2000, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user.username} {self.game} run {self.attempt}'


class Pokemon(models.Model):
  species = models.CharField(max_length=23) # pokeapi species name
  level = models.PositiveSmallIntegerField()
  hp = models.PositiveSmallIntegerField()
  attack = models.PositiveSmallIntegerField()
  defense = models.PositiveSmallIntegerField()
  sp_attack = models.PositiveSmallIntegerField()
  sp_defense = models.PositiveSmallIntegerField()
  speed = models.PositiveSmallIntegerField()
  ability = models.CharField(max_length=30) # TODO: find actual max length
  nature = models.CharField(max_length=7)
  move_1 = models.CharField(max_length=20) # TODO: find actual max length
  move_2 = models.CharField(max_length=20) # TODO: find actual max length
  move_3 = models.CharField(max_length=20) # TODO: find actual max length
  move_4 = models.CharField(max_length=20) # TODO: find actual max length
  run_instance = models.ForeignKey(Run, on_delete=models.CASCADE)

  def __str__(self):
    return self.species