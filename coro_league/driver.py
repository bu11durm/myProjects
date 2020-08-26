# driver to kick off a test

import sqlite3
import os
import pandas as pd
from coro_league.prep_league import setup_the_test
from coro_league.process_new_games import process_new_games
from coro_league.league import League
# from coro_league.league import make_league
import pytest


team_names = ['ZERO', 'LVB', 'BDN', 'FFR', 'PTE']
# season_dir = "data\\2020seas1"
season_dir = "data\\6games"
my_sched = os.path.join(season_dir, 'Sched.csv')
# old_games = [0]
# old_games = [1,2,3]
old_games = [1,2,4,5]

# do i need to do DB connection here?
conn = sqlite3.connect(':memory:')
c = conn.cursor()
my_league = League(c, season_dir, team_names)

setup_the_test(my_league, old_games)

process_new_games(my_league)

# check results
sqlite_select_query = """SELECT * from games"""
c.execute(sqlite_select_query)
records = c.fetchall()
print(records)
sqlite_select_query = """SELECT * from records"""
c.execute(sqlite_select_query)
records = c.fetchall()
print(records)

df = pd.read_sql_query("SELECT * FROM records", conn)
df = df.sort_values('wins', ascending=False)
print(df)

