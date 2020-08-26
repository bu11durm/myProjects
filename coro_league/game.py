import os

class Game:
    def __init__(self, league, game_num, ):
        self.league = league
        self.game_num = game_num
        self.league.c.execute('SELECT visitors from games WHERE gamenum = ?', (game_num,))
        self.visitors = self.league.c.fetchone()[0]
        self.league.c.execute('SELECT hometeam from games WHERE gamenum = ?', (game_num,))
        self.hometeam = self.league.c.fetchone()[0]
        self.league.c.execute('SELECT vis_score from games WHERE gamenum = ?', (game_num,))
        self.vis_score = self.league.c.fetchone()[0]
        self.league.c.execute('SELECT home_score from games WHERE gamenum = ?', (game_num,))
        self.home_score = self.league.c.fetchone()[0]
        self.winner = 'ZERO'
        self.loser = 'ZERO'
        if self.vis_score > self.home_score:
            self.winner = self.visitors
            self.loser = self.hometeam
        elif self.vis_score < self.home_score:
            self.winner = self.hometeam
            self.loser = self.visitors
        # self.validated = False

    def read_game_file(self):
        # self.validated = False
        game_file = 'game' + str(self.game_num) + '.txt'
        game_path = os.path.join(self.league.season_dir, game_file)
        with open(game_path, 'r') as reader:
            game_line1 = reader.readline().split()
            game_line2 = reader.readline().split()
        self.validate_new_game(game_line1[0], game_line2[0])
        self.vis_score = game_line1[1]
        self.home_score = game_line2[1]
        self.set_new_winner(self.vis_score, self.home_score)

    def validate_new_game(self, new_visitors, new_hometeam):
        # validate the teams from the game files match the team in the schedule
        # and validate the scores in the db for each team are initially zero - i.e. game hasn't been mucked with
        assert new_visitors == self.visitors
        assert new_hometeam == self.hometeam
        assert self.vis_score == 0
        assert self.home_score == 0

    def set_new_winner(self, new_vis_score, new_home_score):
        # first check the new game isn't a tie
        assert new_home_score != new_vis_score

        #see which score is higher and set the winner and loser based off that
        if new_vis_score > new_home_score:
            self.winner = self.visitors
            self.loser = self.hometeam
        elif new_vis_score < new_home_score:
            self.winner = self.hometeam
            self.loser = self.visitors

    def commit_results(self):
        self.league.c.execute('UPDATE games SET vis_score = ? WHERE gamenum = ?', (self.vis_score, self.game_num))
        self.league.c.execute('UPDATE games SET home_score = ? WHERE gamenum = ?', (self.home_score, self.game_num))
        self.league.c.execute('SELECT wins from records WHERE team = ?', (self.winner,))
        team_wins = self.league.c.fetchone()[0] + 1
        self.league.c.execute('Update records SET wins = ? WHERE team = ?', (team_wins, self.winner))
        self.league.c.execute('SELECT losses from records WHERE team = ?', (self.loser,))
        team_losses = self.league.c.fetchone()[0] + 1
        self.league.c.execute('Update records SET losses = ? WHERE team = ?', (team_losses, self.loser))