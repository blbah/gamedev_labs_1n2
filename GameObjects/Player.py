from GameObjects.FieldCoord import FieldCoord


def get_for_win(player_number):
    for_win = []
    for i in range(0, 17, 2):
        for_win.append([16 * (player_number - 1), i])
    return for_win


class Player:
    def __init__(self, player_type, player_number):
        self.player_type = player_type
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
        return field[self.current_position.x - 1][self.current_position.y] == 3

    def check_down(self, field):
        return field[self.current_position.x + 1][self.current_position.y] == 3

    def check_right(self, field):
        return field[self.current_position.x][self.current_position.y + 1] == 3

    def check_left(self, field):
        return field[self.current_position.x][self.current_position.y - 1] == 3

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

    def set_places_to_move(self, game_field, list_of_players=None,
                           list_of_possible_moves=None, another_player=None,
                           flag=False):
        if not flag:
            if self.player_number == list_of_players[0].player_number:
                another_player = list_of_players[1]
            else:
                another_player = list_of_players[0]
        if not flag:
            list_of_possible_moves = []
        if self.current_position.x - 2 >= 0:
            if self.check_up(game_field.field):
                if not self.player_check_up(game_field.field,
                                            another_player.current_position):
                    list_of_possible_moves.append(self.up())
                elif self.current_position.x - 3 >= 0 and game_field.field[self.current_position.x - 3][
                    self.current_position.y] == 4 and flag is False:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
                elif self.current_position.x - 4 >= 0\
                        and not game_field.field[self.current_position.x - 3][
                        self.current_position.y] == 4:
                    list_of_possible_moves.append(FieldCoord(
                        self.current_position.x - 4, self.current_position.y))
                    self.is_jump = True
                elif self.current_position.x - 2 == 0:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
        if self.current_position.y + 2 <= 16:
            if self.check_right(game_field.field):
                if not self.player_check_right(game_field.field, another_player.current_position):
                    list_of_possible_moves.append(self.right())
                elif self.current_position.y + 3 <= 16 and game_field.field[self.current_position.x][
                    self.current_position.y + 3] == 4 and flag is False:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
                elif self.current_position.y + 4 <= 16\
                        and not game_field.field[self.current_position.x][
                        self.current_position.y + 3] == 4:
                    list_of_possible_moves.append(FieldCoord(
                        self.current_position.x, self.current_position.y + 4))
                    self.is_jump = True
                elif self.current_position.y + 2 == 16:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
        if self.current_position.x + 2 <= 16:
            if self.check_down(game_field.field):
                if not self.player_check_down(game_field.field, another_player.current_position):
                    list_of_possible_moves.append(self.down())
                elif self.current_position.x + 3 <= 16\
                        and game_field.field[self.current_position.x + 3][
                    self.current_position.y] == 4 and flag is False:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
                elif self.current_position.x + 4 <= 16\
                        and not game_field.field[self.current_position.x + 3][
                        self.current_position.y] == 4:
                    list_of_possible_moves.append(FieldCoord(
                        self.current_position.x + 4, self.current_position.y))
                    self.is_jump = True
                elif self.current_position.x + 2 == 16:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
        if self.current_position.y - 2 >= 0:
            if self.check_left(game_field.field):
                if not self.player_check_left(game_field.field, another_player.current_position):
                    list_of_possible_moves.append(self.left())
                elif self.current_position.y - 3 >= 0\
                        and game_field.field[self.current_position.x][
                    self.current_position.y - 3] == 4 and flag is False:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
                elif self.current_position.y - 4 >= 0\
                        and not game_field.field[self.current_position.x][
                        self.current_position.y - 3] == 4:
                    list_of_possible_moves.append(FieldCoord(self.current_position.x,
                                                             self.current_position.y - 4))
                    self.is_jump = True
                elif self.current_position.y - 2 == 0:
                    self.is_jump = True
                    list_of_possible_moves = another_player\
                        .set_places_to_move(game_field,
                                            list_of_possible_moves=list_of_possible_moves,
                                            another_player=self, flag=True)
        self.places_to_move = list_of_possible_moves
        if not flag:
            jump_list = [FieldCoord(another_player.current_position.x + 2,
                                    another_player.current_position.y),
                         FieldCoord(another_player.current_position.x - 2,
                                    another_player.current_position.y),
                         FieldCoord(another_player.current_position.x,
                                    another_player.current_position.y - 2),
                         FieldCoord(another_player.current_position.x,
                                    another_player.current_position.y + 2)]
            self.jump_list = jump_list
        return list_of_possible_moves

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
