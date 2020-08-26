import sqlite3
import os
import pandas as pd
from process_game import process_a_game


def setup_the_test(my_league, old_games):
# old    def setup_the_test(c, season_dir, old_games, team_names):
    # c is db connection, season_dir is where data is,
    # old_games is list of specific games to process as prep before processing new games
    my_league.c.execute("""CREATE TABLE games (
        gamenum integer,
        visitors text,
        hometeam text,
        vis_score integer,
        home_score integer
        )""")

    my_league.c.execute("""CREATE TABLE records (
        team text,
        wins integer,
        losses integer
        )""")
    # sql_insert =
    for x in range(1, len(my_league.team_names)):
        my_league.c.execute('INSERT INTO records (team, wins, losses) VALUES (?, ?, ?)', (my_league.team_names[x], 0, 0))
    # print('current dir is ' + os.getcwd())
    season_dir = my_league.season_dir
    my_sched = os.path.join(season_dir, 'Sched.csv')
    gameCols = ['GameNum', 'Visitor', 'Home']
    dfSched = pd.read_csv(my_sched, index_col='GameNum', usecols=gameCols)
    # sql_insert = 'INSERT INTO records (gamenum, visitors, hometeam, vis_score, home_score) VALUES (?, ?, ?, ?, ?)', (x, team_names[dfSched.iloc[x-1,0]], team_names[dfSched.iloc[x-1,1]],0, 0)
    for x in range(1, dfSched.shape[0] + 1):
        my_league.c.execute('INSERT INTO games (gamenum, visitors, hometeam, vis_score, home_score) VALUES (?, ?, ?, ?, ?)',
                  (x, my_league.team_names[dfSched.iloc[x - 1, 0]], my_league.team_names[dfSched.iloc[x - 1, 1]], 0, 0))

    sqlite_select_query = """SELECT * from games"""
    my_league.c.execute(sqlite_select_query)
    records = my_league.c.fetchall()
    sqlite_select_query = """SELECT * from records"""
    my_league.c.execute(sqlite_select_query)
    records = my_league.c.fetchall()

    if old_games[0] > 0:
        for game_num in old_games:
            process_a_game(my_league, game_num)
    return


