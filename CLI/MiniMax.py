import copy

from infinity import inf

from GameObjects.FieldCoord import FieldCoord
from GameObjects.Wall import Wall


counter = 0


def minimax(obj_minimax, depth, alpha, beta, maximizingPlayer, first_player, second_player):
    global counter
    counter += 1
    if depth == 0:
        path_first, path_second = None
        path_first = min(path_first, key=len)
        path_second = min(path_second, key=len)
        obj_minimax.player_one_path = path_first
        obj_minimax.player_two_path = path_second
        return evaluation(obj_minimax)


def run_minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two):
    evl, act = minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two)
    global counter
    print(counter)
    counter = 0
    for kid in act.child:
        if kid.minimax_eval == evl:
            return kid.action


def evaluation(minim):
    minim.minimax_eval = len(minim.player_one_path) - len(minim.player_two_path)
    return minim.minimax_eval, minim


class Minimax:
    def __init__(self, field, first_player, second_player, action=None, depth=+inf, parent=None):
        self.game_field = field
        self.first_player = first_player
        self.second_player = second_player
        self.action = action
        self.depth = depth
        self.minimax_eval = None
        self.child = []
        self.parent = None
        self.player_one_path = None
        self.player_two_path = None

