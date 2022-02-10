import sys

from CLI.OutputWriter import print_field, send_jump, send_move
from CLI.InputReader import do as do
from GameObjects.GameField import GameField
from GameObjects.Player import Player


def start():
    game_field = GameField()
    player_one = Player(True, 1)
    player_two = Player(True, 2)
    list_of_players = [player_one, player_two]
    counter = 0
    moves = 0
    while not player_one.is_win() or not player_two.is_win():
        game(list_of_players[counter], game_field, list_of_players)
        if player_one.is_win() or player_two.is_win():
            sys.exit()
        moves += 1
        counter = 1 if counter == 0 else 0
    sys.exit()

def player_move(player, game_field, list_of_players):
    player.set_places_to_move(game_field, list_of_players)
    try:
        move_player_input = do(player, "move")
        if player.action is not None:
            move_player_input = move_player_input.is_in(player.places_to_move)
        if move_player_input == "back":
            game(player, game_field, list_of_players)
        player.set_next_position(player.places_to_move[int(move_player_input) - 1])
        if player.can_move_here:
            game_field.move_player(player)
            if player.is_jump and player.player_type is False\
                    and player.current_position.is_in(
                    player.jump_list) is not None:
                send_jump(player)
            elif player.player_type is False:
                send_move(player)
            player.is_jump = False
            player.jump_list = None
            player.action = None
        else:
            player_move(player, game_field, list_of_players)
    except Exception:
        pass

def game(player, game_field, list_of_players):
    print_field(game_field.field)
    game_input = do(player, "choose", game_field, list_of_players)
    if game_input == "1":
        player_move(player, game_field, list_of_players)
    else:
        game(player, game_field, list_of_players)


if __name__ == '__main__':
    start()