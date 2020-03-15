from .action import Action
from engine.console_player import ConsolePlayer
from engine.dealer import Dealer
from engine.game_settings import DefaultGameSettings
from engine.round import Round
from engine.seating import Seating


def action_check_call():
    def player_action_call(amount):
        return Action.ACTION_CALL, amount

    return player_action_call


game_setings = DefaultGameSettings()
for player in game_setings.players:
    if player is not ConsolePlayer:
        player.act = action_check_call()
seating = Seating(game_setings.players)
dealer = Dealer(None, seating)
round = Round(dealer)
round.play_round(game_setings.small_blind_size)