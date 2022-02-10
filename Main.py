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

def game(player, game_field, list_of_players):
    print_field(game_field.field)
    game_input = do(player, "choose", game_field, list_of_players)
    if game_input == "1":
        player_move(player, game_field, list_of_players)
    else:
        game(player, game_field, list_of_players)


if __name__ == '__main__':
    start()