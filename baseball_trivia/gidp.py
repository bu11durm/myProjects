import pandas as pd
playerCols = ['playerID','nameLast','nameFirst', 'bats']
# dfPlayer = pd.read_csv ('C:\\bakework\\baseballdatabank-master\\core\\people.csv', index_col='playerID', usecols=playerCols)
dfPlayer = pd.read_csv ('data\people.csv', index_col='playerID', usecols=playerCols)


dfPlayer.nameFirst.fillna('', inplace=True)
dfPlayer['PlayerName'] = dfPlayer['nameFirst'].str.cat(dfPlayer['nameLast'], sep=' ')
gcols = ['yearID', 'playerID', 'GIDP']
# df1 = pd.read_csv ('C:\\bakework\\baseballdatabank-master\\core\\Batting.csv',
df1 = pd.read_csv('data\Batting.csv',
                   index_col=['yearID'], usecols=gcols)
for i in range(1932,2019):
    df2 = df1.loc[1932:i].groupby('playerID').sum().sort_values('GIDP', ascending=False).join(dfPlayer)
    print ("Year: " + str(i) + "; Player: " + df2.iloc[0,1] + " " + df2.iloc[0,2] + "; GIDP: " + str(df2.iloc[0,0]))
