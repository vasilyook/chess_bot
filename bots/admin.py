from django.contrib import admin
from .bot import Bot
from .models import User
from .models import Game
from .models import Division


class GameAdmin(admin.ModelAdmin):
    fields = ['tour', 'division', 'player', 'opponent', 'player_score', 'opponent_score', 'links']
    list_display = ('tour', 'division', 'player', 'opponent', 'player_score', 'opponent_score')
    list_filter = ['tour', 'division', 'player', 'opponent']
    # search_fields = ['player', 'opponent']
admin.site.register(User)
admin.site.register(Game, GameAdmin)
admin.site.register(Division)

# Register your models here.
