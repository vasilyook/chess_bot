from django.db import models
from django.contrib import admin

class TelegramUser(models.Model):
	name = models.CharField(max_length=200)
	telegram_id = models.BigIntegerField(default=None)
	last_command = models.CharField(max_length=20, null=True)

class User(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Division(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Game(models.Model):
	player = models.ForeignKey(User, on_delete=models.PROTECT, related_name='player')
	opponent = models.ForeignKey(User, on_delete=models.PROTECT, related_name='opponent')
	links = models.CharField(max_length=200)
	player_score = models.DecimalField(max_digits=2, decimal_places=1)
	opponent_score = models.DecimalField(max_digits=2, decimal_places=1)
	tour = models.IntegerField()
	division = models.ForeignKey(Division, on_delete=models.PROTECT)

	@admin.display(
		boolean=True,
		ordering='tour',
	)

	def __str__(self):
		text = "Тур " + str(self.tour) +': '+str(self.player.name) +' - '+ str(self.opponent.name)
		return text
	@property
	def get_links(self):
		return self.links.split(',')
# Create your models here.