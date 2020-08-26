
class League:
    def __init__(self, db_conn, season_dir, team_names, ):
        self.c = db_conn
        self.season_dir = season_dir
        self.team_names = team_names

# don't think this is needed anymore
# def make_league(db_conn, season_dir, team_names):
#     league = League(db_conn, season_dir, team_names)
#     return league