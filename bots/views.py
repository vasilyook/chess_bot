from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .chess import Chess
import json
import os
from .models import Game
from django.shortcuts import  render

def index(request):
    saved_games = Game.objects.order_by('-id')
    context = {'saved_games': saved_games}
    return render(request, 'games/index.html', context)


load_dotenv()
token = os.getenv("TOKEN")

@csrf_exempt
def webhook(request):
    update = json.loads(request.body)
    Chess(token).handle(update)
    return JsonResponse({"message": "ok"})
