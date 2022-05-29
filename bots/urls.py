from django.urls import path

from . import views
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

urlpatterns = [
    path('games', views.index, name='index'),
    path('webhooks/telegram' + token, views.webhook),
]