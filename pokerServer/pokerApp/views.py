from django.http import JsonResponse
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from engine.game_settings import DefaultGameSettings
from .poker_player import PokerPlayer


@renderer_classes(JSONRenderer)
def get_settings(request):
    settings = DefaultGameSettings()
    player = PokerPlayer()
    return JsonResponse(player)
