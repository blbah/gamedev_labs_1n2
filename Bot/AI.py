from infinity import inf

from Bot import Minimax
from GameObjects.Wall import Wall


def put_wall():
    return f"{ai_action.coordinate.coordinates_start.x} " \
           f"{ai_action.coordinate.coordinates_start.y} " \
           f"{ai_action.coordinate.coordinates_end.x} " \
           f"{ai_action.coordinate.coordinates_end.y}"


def move(player):
    for index, step in enumerate(player.places_to_move):
        if step.x == ai_action.coordinate.x\
                and step.y == ai_action.coordinate.y:
            return index + 1


def choose(player, field, players_list):
    bot_doing = Minimax.run_minimax(field, depth=2, alpha=-inf, beta=+inf,
                                    maximizingPlayer=True, player_one=player,
                                    player_two=players_list[1] if players_list[0]
                                    .player_number == player.player_number
                                     else players_list[0])
    if type(bot_doing) == Wall or type(bot_doing) == Wall:
        ai_action.action = "2"
        ai_action.coordinate = bot_doing
    else:
        ai_action.action = "1"
        ai_action.coordinate = bot_doing
    return ai_action.action


class AI:
    def __init__(self, operation, coordinate):
        self.action = operation
        self.coordinate = coordinate


ai_action = AI(None, None)