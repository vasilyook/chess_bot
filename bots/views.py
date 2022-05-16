from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .chess import Chess
import json
import os

load_dotenv()
token = os.getenv("TOKEN")

def index(request):
    return JsonResponse({"message": "ok"})

@csrf_exempt
def webhook(request):
    update = json.loads(request.body)
    Chess(token).handle(update)
    return JsonResponse({"message": "ok"})
