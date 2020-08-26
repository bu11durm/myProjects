import os
from process_game import process_a_game
# from coro_league.league import League

def process_new_games(my_league):
#    print(my_league)
    for game_num in range(1, 21):
        game_file = 'game' + str(game_num) + '.txt'
        game_path = os.path.join(my_league.season_dir, game_file)
        my_league.c.execute('SELECT * from games WHERE gamenum = ?', (game_num,))
        this_game = (my_league.c.fetchone())
        if ((this_game[3] + this_game[4]) == 0) and (os.path.isfile(game_path)):
            process_a_game(my_league, game_num)
    return