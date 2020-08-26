# driver to kick off a test

import os
import sqlite3

# from coro_league.league import League
from league import make_league
# from coro_league.prep_league import setup_the_test
from process_new_games import process_new_games

# import pandas as pd
from prep_league import setup_the_test


def test_two_new():
    # arrange
    team_names = ['ZERO', 'LVB', 'BDN', 'FFR', 'PTE']
    season_dir = "data\\6games"
    my_sched = os.path.join(season_dir, 'sched.csv')
    old_games = [1, 2, 4, 5]

    # do i need to do DB connection here?
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    my_league = make_league(c, season_dir, team_names)

    # act
    setup_the_test(my_league, old_games)
    process_new_games(my_league)

    # check results
#    sqlite_select_query = """SELECT * from records"""
#    c.execute(sqlite_select_query)
#    records = c.fetchall()
#    print(records)

    #    df = pd.read_sql_query("SELECT * FROM records", conn)
    #    df = df.sort_values('wins', ascending=False)
    #    print(df)

    # assert
    assert records[0][1] == 2
