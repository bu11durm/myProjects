import pandas as pd
playerCols = ['playerID','nameLast','nameFirst', 'debut', 'finalGame']
dfPlayer = pd.read_csv ('data\people.csv', index_col='playerID', usecols=playerCols)

dfPlayer.nameFirst.fillna('', inplace=True)
dfPlayer['PlayerName'] = dfPlayer['nameFirst'].str.cat(dfPlayer['nameLast'], sep=' ')
gcols = ['yearID', 'playerID', 'POS', 'InnOuts']
df1 = pd.read_csv ('data\Fielding.csv',
                   index_col=['yearID'], usecols=gcols)
# for i in range(1932,2019):
positions = ['C', '1B', '2B', '3B', 'SS', 'OF', 'P']

for player_pos in positions:
    df2 = df1[df1['POS'] == player_pos]
    df2 = df2.groupby('playerID').sum().sort_values('InnOuts', ascending=False).join(dfPlayer)
    firstgame = df2.iloc[0,3].split('-')
    lastgame = df2.iloc[0,4].split('-')
    print("Position: " + player_pos + "; Player: " + df2.iloc[0,1] + " " + df2.iloc[0,2] + "; Defensive Innings: " + str(df2.iloc[0,0]) + " " + firstgame[0] + "-" + lastgame[0])
    firstgame = df2.iloc[1,3].split('-')
    lastgame = df2.iloc[1,4].split('-')
    print("Position: " + player_pos + "; Player: " + df2.iloc[1, 1] + " " + df2.iloc[1, 2] + "; Defensive Innings: " + str(df2.iloc[1, 0]) + " " + firstgame[0] + "-" + lastgame[0])
    if player_pos == 'OF':
        firstgame = df2.iloc[2, 3].split('-')
        lastgame = df2.iloc[2, 4].split('-')
        print("Position: " + player_pos + "; Player: " + df2.iloc[2, 1] + " " + df2.iloc[2, 2] + "; Defensive Innings: " + str(df2.iloc[2, 0]) + " " + firstgame[0] + "-" + lastgame[0])
        firstgame = df2.iloc[3, 3].split('-')
        lastgame = df2.iloc[3, 4].split('-')
        print("Position: " + player_pos + "; Player: " + df2.iloc[3, 1] + " " + df2.iloc[3, 2] + "; Defensive Innings: " + str(df2.iloc[3, 0]) + " " + firstgame[0] + "-" + lastgame[0])
        firstgame = df2.iloc[4, 3].split('-')
        lastgame = df2.iloc[4, 4].split('-')
        print("Position: " + player_pos + "; Player: " + df2.iloc[4, 1] + " " + df2.iloc[4, 2] + "; Defensive Innings: " + str(df2.iloc[4, 0]) + " " + firstgame[0] + "-" + lastgame[0])
        firstgame = df2.iloc[5, 3].split('-')
        lastgame = df2.iloc[5, 4].split('-')
        print("Position: " + player_pos + "; Player: " + df2.iloc[5, 1] + " " + df2.iloc[5, 2] + "; Defensive Innings: " + str(df2.iloc[5, 0]) + " " + firstgame[0] + "-" + lastgame[0])
