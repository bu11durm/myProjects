import sqlite3
import os
from game import Game

def process_a_game(my_league, game_num):
    # create a game object
    # read game info from file
    # -- validate the game
    # -- in read, figure out winner
    # update the database

    game = Game(my_league, game_num)
    game.read_game_file()
    game.commit_results()

    return

