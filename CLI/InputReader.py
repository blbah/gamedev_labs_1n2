from GameObjects.FieldCoord import FieldCoord


def do(player, types, field=None, players_list=None):
    if types == "wall":
        return wall_case(player)
    elif types == "move":
        return move_case(player)
    elif types == "choose":
        return choose_case(player, field, players_list)
    elif types == "playAgain":
        if player.player_type:
            return "1"


def wall_case(player):
    return player.action[1]


def move_case(player):
    return player.action[1]


def choose_case(player, field, players_list):
    player.action = shift_player(input().split(" "))
    return player.action[0]


def shift_player(temp):
    if temp[0] == "move" or temp[0] == "jump":
        temp[0] = "1"
        temp[1] = FieldCoord(2 * (int(temp[1][1]) - 1), 2 * (ord(temp[1][0].lower()) - 97))
    elif temp[0] == "wall":
        temp[0] = '2'
        if temp[1][2] == 'h':
            x = ((ord(temp[1][0].lower()) - 96 - 18) * 2) - 1
            y = ((int(temp[1][1])) * 2) - 1
            temp[1] = f"{y} {x - 1} {y} {x + 1}"
        else:
            x = ((ord(temp[1][0].lower()) - 96 - 18) * 2) - 1
            y = ((int(temp[1][1])) * 2) - 1
            temp[1] = f"{y - 1} {x} {y + 1} {x}"
    return temp
