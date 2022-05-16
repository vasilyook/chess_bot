from django.db import models

class TelegramUser(models.Model):
	name = models.CharField(max_length=200)
	telegram_id = models.BigIntegerField(default=None)
	last_command = models.CharField(max_length=20, null=True)

class User(models.Model):
	name = models.CharField(max_length=200)

class Division(models.Model):
	name = models.CharField(max_length=20)

class Game(models.Model):
	player = models.ForeignKey(User, on_delete=models.PROTECT, related_name='player')
	opponent = models.ForeignKey(User, on_delete=models.PROTECT, related_name='opponent')
	links = models.CharField(max_length=200)
	player_score = models.DecimalField(max_digits=2, decimal_places=1)
	opponent_score = models.DecimalField(max_digits=2, decimal_places=1)
	tour = models.IntegerField()
	division = models.ForeignKey(Division, on_delete=models.PROTECT)
# Create your models here.
