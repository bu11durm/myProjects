import os
from matplotlib import pyplot as plt
import pandas as pd

weeks = 10
game_num = 0
season_dir = "data\\2020seas1"
wins = [0] * 5
team_names = ['ZERO', 'LVB', 'BDN', 'FFR', 'PTE']
line1 = [0]
line2 = [0]
line3 = [0]
line4 = [0]
cur_week = [0]

for week in range(1,weeks+1):
    for x in range(1,3):
        game_num += 1
        game_file = 'game' + str(game_num) + '.txt'
        game_path = os.path.join(season_dir, game_file)
        with open(game_path, 'r') as cur_game:
            game_line1 = cur_game.readline().split()
            game_line2 = cur_game.readline().split()
        if int(game_line1[1]) < int(game_line2[1]):
            wins[team_names.index(game_line2[0])] += 1
        else:
            wins[team_names.index(game_line1[0])] += 1

    cur_week.append(week)
    line1.append(wins[1])
    line2.append(wins[2])
    line3.append(wins[3])
    line4.append(wins[4])

# df = pd.DataFrame({'cur_week':cur_week})
# df['line1'] = line1
# df['line2'] = line2
# df['line3'] = line3
# df['line4'] = line4
# df.plot(kind='line',x='cur_week',y='line1')
# print(df)

plt.plot(cur_week, line1, label='Boats')
plt.plot(cur_week, line2, label='Dozens')
plt.plot(cur_week, line3, label='Furters')
plt.plot(cur_week, line4, label='Eaters')
plt.xlabel('Week')
plt.ylabel('Wins')
plt.legend()
plt.title('Corona League Wins')

plt.show()



