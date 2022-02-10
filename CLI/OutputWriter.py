symbols = ["\033[32m {}".format(" "),
           "\033[31m {}".format("1"),
           "\033[31m {}".format("2"),
           "\033[37m {}".format("∎"),
           "\033[33m {}".format("∎"),
           "\033[33m {}".format("#")]


def choose_play_mode():
    print("Choose play mode:"
          "\n1) Human VS Human"
          "\n2) Human VS Bot"
          "\n3) Bot   VS Bot")
    pass


def choose_your_color():
    print("Choose your color:"
          "\n1) White"
          "\n2) Black")
    pass


def win_message(player, field):
    print_field(field)
    print(f"The player number {player.player_number} won!")
    pass


def print_field(field):
    a = 1
    if a == 0:
        horizontal(field)
        rows(field)
    else:
        for index, i in enumerate(field):
            for index2, j in enumerate(i):
                print(symbols[j], end="")
            print()
    pass


def horizontal(field):
    num_horizontal = "    "
    counter = 0
    for _ in field[0]:
        if counter < 10:
            num_horizontal += f"{counter}  "
            counter += 1
        else:
            num_horizontal += f"{counter} "
            counter += 1
    print(num_horizontal)

    num_horizontal = "     "
    counter = 0
    for item in field[0]:
        if item == 0 or item == 1 or item == 2:
            num_horizontal += f"{counter}"
            counter += 1
        else:
            num_horizontal += "     "
    print(num_horizontal)


def rows(field):
    counter_1 = 0
    counter_2 = 0
    for row in field:
        if row[0] == 0 or row[0] == 1 or row[0] == 2:
            if counter_2 < 10:
                print(f"{counter_2}  {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1
            else:
                print(f"{counter_2} {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1

        else:
            if counter_2 < 10:
                print(f"{counter_2}   {row}")
                counter_2 += 1
            else:
                print(f"{counter_2}  {row}")
                counter_2 += 1


def send_wall(wall):
    if wall.coordinates_start.x == wall.coordinates_end.x:
        print(f"wall {chr(int(wall.coordinates_middle.y / 2 + 96 + 19)).capitalize()}"
              f"{int((wall.coordinates_middle.x + 1) / 2)}h")
    else:
        print(f"wall {chr(int(wall.coordinates_middle.y / 2 + 96 + 19)).capitalize()}"
              f"{int((wall.coordinates_middle.x + 1) / 2)}v")


def send_move(player):
    print(f"move {chr(int(player.current_position.y / 2 + 96) + 1).capitalize()}"
          f"{int(player.current_position.x / 2) + 1}")


def send_jump(player):
    print(f"jump {chr(int(player.current_position.y / 2 + 96) + 1).capitalize()}"
          f"{int(player.current_position.x / 2) + 1}")
