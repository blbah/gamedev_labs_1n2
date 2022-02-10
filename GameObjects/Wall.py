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
        self.is_there_path_to_win = None

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
