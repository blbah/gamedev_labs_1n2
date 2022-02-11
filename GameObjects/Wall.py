import copy

from GameObjects.FieldCoord import FieldCoord


def if_there_path_to_win(game_field, player1, player2, wall):
    game_field.graph.cleanup()
    temp_field = copy.deepcopy(game_field)
    temp_field.set_wall(wall)
    temp_field.graph = temp_field.set_graph()
    if temp_field.path_finder([player1, player2]):
        del temp_field
        return True
    else:
        del temp_field
        return False


class Wall:
    def __init__(self, coordinates_start, coordinates_end, game_field):
        self.coordinates_start = coordinates_start
        self.coordinates_end = coordinates_end
        self.coordinates_middle = self.set_coordinates_middle()
        self.is_length_correct = self.if_length_correct()
        self.between_two_pares = self._if_between_two_pares(game_field)
        self.is_there_another_wall = self._if_there_another_wall(game_field.field)
        self.is_there_path_to_win = None

    def _if_between_two_pares(self, game_field):
        if self.coordinates_start.y == self.coordinates_end.y:
            return game_field.field[self.coordinates_start.x][self.coordinates_start.y - 1] in [0, 1, 2] and \
                   game_field.field[self.coordinates_start.x][self.coordinates_start.y + 1] in [0, 1, 2] and \
                   game_field.field[self.coordinates_start.x][self.coordinates_end.y - 1] in [0, 1, 2] and \
                   game_field.field[self.coordinates_start.x][self.coordinates_end.y + 1] in [0, 1, 2]
        elif self.coordinates_start.x == self.coordinates_end.x:
            return game_field.field[self.coordinates_start.x - 1][self.coordinates_start.y] in [0, 1, 2] and \
                   game_field.field[self.coordinates_start.x + 1][self.coordinates_start.y] in [0, 1, 2] and \
                   game_field.field[self.coordinates_end.x - 1][self.coordinates_start.y] in [0, 1, 2] and \
                   game_field.field[self.coordinates_end.x + 1][self.coordinates_start.y] in [0, 1, 2]

    def _if_there_another_wall(self, game_field):
        return game_field[self.coordinates_start.x][self.coordinates_start.y] == 4 or \
               game_field[self.coordinates_end.x][self.coordinates_end.y] == 4 or \
               game_field[self.coordinates_middle.x][self.coordinates_middle.y] == 4

    def set_coordinates_middle(self):
        if self.coordinates_start.y == self.coordinates_end.y:
            if self.coordinates_start.x > self.coordinates_end.x:
                return FieldCoord(self.coordinates_end.x + 1, self.coordinates_start.y)
            else:
                return FieldCoord(self.coordinates_start.x + 1, self.coordinates_start.y)
        else:
            if self.coordinates_start.y > self.coordinates_end.y:
                return FieldCoord(self.coordinates_start.x, self.coordinates_end.y + 1)
            else:
                return FieldCoord(self.coordinates_start.x, self.coordinates_start.y + 1)

    def if_length_correct(self):
        if self.coordinates_start.x == self.coordinates_end.x:
            if self.coordinates_start.y > self.coordinates_end.y:
                return len([num for num in range(self.coordinates_end.y + 1,
                                                 self.coordinates_start.y)]) == 1
            else:
                return len([num for num in range(self.coordinates_start.y + 1,
                                                 self.coordinates_end.y)]) == 1
        elif self.coordinates_start.y == self.coordinates_end.y:
            if self.coordinates_start.x > self.coordinates_end.x:
                return len([num for num in range(self.coordinates_end.x + 1,
                                                 self.coordinates_start.x)]) == 1
            else:
                return len([num for num in range(self.coordinates_start.x + 1,
                                                 self.coordinates_end.x)]) == 1
        else:
            return False
