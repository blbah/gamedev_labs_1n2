field_nums = [100, 49, 49, 100, 0, 0]


def get_connected_points(field):
    connected_points = []
    for i in range(0, len(field), 2):
        for j in range(0, len(field[i]), 2):
            if i != len(field) - 1 and j != len(field) - 1:
                if field[i][j + 1] == 3:
                    connected_points.append(
                        (i // 2, j // 2), (i // 2, j // 2 + 1))
                if field[i + 1][j] == 3:
                    connected_points.append(
                        (i // 2, j // 2), (i // 2 + 1, j // 2))
            else:
                if i == len(field) - 1 and j != len(field) - 1:
                    if field[i][j + 1] == 3:
                        connected_points.append(
                            ((i // 2, j // 2), (i // 2, j // 2 + 1)))
                if j == len(field) - 1 and i != len(field) - 1:
                    if field[i + 1][j] == 3:
                        connected_points.append(
                            ((i // 2, j // 2), (i // 2 + 1, j // 2)))
    return connected_points


def fill_the_field():
    field = []

    for row_index in range(9):
        if row_index != 8:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
            field.append([3 for i in range(17)])
        else:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
    for i in range(16):
        for j in range(16):
            if i % 2 == 1 and j % 2 == 1:
                field[i][j] = 5
    return field


def field_preparation(field):
    center_real = 8
    field[0][center_real] = 2
    field[-1][center_real] = 1
    return field


class GameField:
    def __init__(self):
        self.field = self.get_start_field()

    def game_over(self):
        return True if 1 in self.field[0] or 2 in self.field[-1] else False

    @staticmethod
    def get_start_field():
        return field_preparation(fill_the_field())

    def path_finder(self, players):
        pass

    @staticmethod
    def graph_prepare(field):
        temp_field = []
        for i in range(len(field[0])):
            temp_field.append([])
            for j in range(len(field[1])):
                temp_field[i].append(field_nums[field[i][j]])
        return temp_field

    def set_wall(self, wall):
        self.field[wall.coordinates_start.x][wall.coordinates_start.y] = 4
        self.field[wall.coordinates_end.x][wall.coordinates_end.y] = 4
        self.field[wall.coordinates_middle.x][wall.coordinates_middle.y] = 4

    def move_player(self, player):
        self.field[player.current_position.x][player.current_position.y] = 0
        self.field[player.next_position.x][player.next_position.y] = player.player_number
        player.current_position = player.next_position
