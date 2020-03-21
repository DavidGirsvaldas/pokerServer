from django.urls import path
from .api_views import PlayersView

app_name = "pokerApp"
urlpatterns = [
    path("players/", PlayersView.as_view(), name="get_players")
]
