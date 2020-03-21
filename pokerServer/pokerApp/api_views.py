from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from engine.player import Player
from .serializers import PlayerSerializer


class PlayersView(APIView):

    @renderer_classes([JSONRenderer])
    def get(self, request):
        player = Player("test", 100)
        serialized = PlayerSerializer(player).data
        return Response(serialized)
