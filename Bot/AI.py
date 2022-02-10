from GameObjects.Wall import Wall


def move(player):
    for index, step in enumerate(player.places_to_move):
        if step.x == ai_action.coordinate.x\
                and step.y == ai_action.coordinate.y:
            return index + 1


def choose(player, field, players_list):
    bot_doing = None
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