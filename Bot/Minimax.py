import copy

from infinity import inf

from GameObjects.FieldCoord import FieldCoord
from GameObjects.Wall import Wall


counter = 0


def run_minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two):
    evl, act = minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two)
    global counter
    print(counter)
    counter = 0
    for kid in act.child:
        if kid.minimax_eval == evl:
            return kid.action


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

    if type(obj_minimax) != Minimax:
        obj_minimax = Minimax(copy.deepcopy(obj_minimax), first_player, second_player, action=None, depth=depth)
    path_first, path_second = None
    path_first = min(path_first, key=len)
    path_second = min(path_second, key=len)
    obj_minimax.player_one_path = path_first
    obj_minimax.player_two_path = path_second
    walls = all_walls(obj_minimax.game_field, first_player, second_player, path_second)
    for wall in walls:
        obj_minimax.child.append(Minimax(wall[0], wall[1], wall[2], wall[3], depth, obj_minimax))
    next_move_one_player = all_moves(obj_minimax.game_field, first_player, second_player, path_first)
    obj_minimax.child.append(
        Minimax(next_move_one_player[0][0], next_move_one_player[0][1], next_move_one_player[0][2],
                next_move_one_player[0][3]))

    if maximizingPlayer:
        max_eval = -inf
        for child_local in obj_minimax.child:
            eval, act = minimax(child_local, depth - 1, alpha, beta, False, second_player, first_player)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            obj_minimax.minimax_eval = alpha
            if beta <= alpha:
                break
        return max_eval, obj_minimax

    else:
        min_eval = +inf
        for child_local in obj_minimax.child:
            eval, act = minimax(child_local, depth - 1, alpha, beta, True, first_player, second_player)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            obj_minimax.minimax_eval = beta
            if beta <= alpha:
                break
        return min_eval, obj_minimax


def evaluation(minim):
    minim.minimax_eval = len(minim.player_one_path) - len(minim.player_two_path)
    return minim.minimax_eval, minim


def all_walls(game_field, player_one, player_two, path_to_win):
    game_fields = []
    if player_one.walls_amount > 0:
        walls = []
        del path_to_win[0::2]
        for wall in path_to_win:
            if wall[0] % 2 == 0:
                if wall[0] - 2 >= 0:
                    walls.append(Wall(FieldCoord(wall[1], wall[0]), FieldCoord(wall[1], wall[0] - 2), game_field))
                if wall[0] + 2 <= 16:
                    walls.append(Wall(FieldCoord(wall[1], wall[0]), FieldCoord(wall[1], wall[0] + 2), game_field))
            else:
                if wall[1] - 2 >= 0:
                    walls.append(Wall(FieldCoord(wall[1], wall[0]), FieldCoord(wall[1] - 2, wall[0]), game_field))
                if wall[1] + 2 <= 16:
                    walls.append(Wall(FieldCoord(wall[1], wall[0]), FieldCoord(wall[1] + 2, wall[0]), game_field))

    return game_fields


def all_moves(field, first_player, second_player, way):
    game_fields = []
    tem_field = copy.deepcopy(field)
    tem_player = copy.deepcopy(first_player)
    tem_two_player = copy.deepcopy(second_player)
    tem_player.set_places_to_move(field, [tem_player, tem_two_player])
    ind = -1
    for index, step in enumerate(tem_player.places_to_move):
        if step.x == way[2][1] and step.y == way[2][0]:
            ind = index
            break
    tem_player.set_next_position(tem_player.places_to_move[ind])
    if tem_player.can_move_here:
        tem_field.move_player(tem_player)
        game_fields.append((tem_field, tem_player, tem_two_player, tem_player.next_position))
    return game_fields
