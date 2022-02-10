from GameObjects.FieldCoord import FieldCoord


def get_for_win(player_number):
    for_win = []
    for i in range(0, 17, 2):
        for_win.append([16 * (player_number - 1), i])
    return for_win


class Player:
    def __init__(self, player_type, player_number):
        self.player_type = True
        self.player_number = player_number
        self.walls_amount = 10
        self.current_position = self._set_start_position()
        self.next_position = None
        self.can_move_here = None
        self.places_to_move = None
        self.action = None
        self.jump_list = None
        self.is_jump = False
        self._for_win = get_for_win(self.player_number)

    def up(self):
        return FieldCoord(self.current_position.x - 2,
                          self.current_position.y)

    def down(self):
        return FieldCoord(self.current_position.x + 2,
                          self.current_position.y)

    def left(self):
        return FieldCoord(self.current_position.x,
                          self.current_position.y - 2)

    def right(self):
        return FieldCoord(self.current_position.x,
                          self.current_position.y + 2)

    def check_up(self, field):
        return field[self.current_position.x - 1]
        [self.current_position.y] == 3

    def check_down(self, field):
        return field[self.current_position.x + 1]
        [self.current_position.y] == 3

    def check_right(self, field):
        return field[self.current_position.x]
        [self.current_position.y + 1] == 3

    def check_left(self, field):
        return field[self.current_position.x]
        [self.current_position.y - 1] == 3

    def player_check_up(self, field, second_player):
        return self.current_position.x - 2 == second_player.x \
               and self.current_position.y == second_player.y

    def player_check_down(self, field, second_player):
        return self.current_position.x + 2 == second_player.x \
               and self.current_position.y == second_player.y

    def player_check_right(self, field, second_player):
        return self.current_position.x == second_player.x \
               and self.current_position.y + 2 == second_player.y

    def player_check_left(self, field, second_player):
        return self.current_position.x == second_player.x \
               and self.current_position.y - 2 == second_player.y

    def is_win(self):
        if self.player_number == 1:
            if self.current_position.x == 0:
                return True
        if self.player_number == 2:
            if self.current_position.x == 16:
                return True
        return False

    def _set_start_position(self):
        return FieldCoord(16, 8) if self.player_number == 1 else FieldCoord(0, 8)

    def decrease_wall_amount(self):
        if self.walls_amount != 0:
            self.walls_amount -= 1

    def set_next_position(self, coordinate):
        for places in self.places_to_move:
            if coordinate.is_correct and coordinate.x == places.x and coordinate.y == places.y:
                self.next_position = coordinate
                self.can_move_here = True
                break
            else:
                self.next_position = None
                self.can_move_here = False

    @property
    def for_win(self):
        return self._for_win
