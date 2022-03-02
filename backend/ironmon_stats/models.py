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
  user = models.ForeignKey(User, related_name='runs', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user.username} {self.game} run {self.attempt}'


class Pokemon(models.Model):
  species = models.CharField(max_length=23) # pokeapi species name
  level = models.PositiveSmallIntegerField(blank=True)
  hp = models.PositiveSmallIntegerField(blank=True)
  attack = models.PositiveSmallIntegerField(blank=True)
  defense = models.PositiveSmallIntegerField(blank=True)
  sp_attack = models.PositiveSmallIntegerField(blank=True)
  sp_defense = models.PositiveSmallIntegerField(blank=True)
  speed = models.PositiveSmallIntegerField(blank=True)
  ability = models.CharField(max_length=30, blank=True) # TODO: find actual max length
  nature = models.CharField(max_length=7, blank=True)
  move_1 = models.CharField(max_length=20, blank=True) # TODO: find actual max length
  move_2 = models.CharField(max_length=20, blank=True) # TODO: find actual max length
  move_3 = models.CharField(max_length=20, blank=True) # TODO: find actual max length
  move_4 = models.CharField(max_length=20, blank=True) # TODO: find actual max length
  run_instance = models.ForeignKey(Run, related_name='pokemon', on_delete=models.CASCADE)

  def __str__(self):
    return self.species