import pandas as pd
playerCols = ['playerID','nameLast','nameFirst', 'bats']
dfPlayer = pd.read_csv ('data\people.csv', index_col='playerID', usecols=playerCols)

dfPlayer.nameFirst.fillna('', inplace=True)
dfPlayer['PlayerName'] = dfPlayer['nameFirst'].str.cat(dfPlayer['nameLast'], sep=' ')
gcols = ['yearID', 'playerID', 'GP']
df1 = pd.read_csv ('data\AllstarFull.csv',
                   index_col=['yearID'], usecols=gcols)

df2 = df1[df1['GP'] == 0]
df2 = df2.groupby('playerID').count().sort_values('GP', ascending=False).join(dfPlayer)
print(df2.iloc[0,1] + " " + df2.iloc[0,2] + " did not play in " + str(df2.iloc[0,0]) + " all-star games")
print(df2.iloc[1,1] + " " + df2.iloc[1,2] + " did not play in " + str(df2.iloc[1,0]) + " all-star games")
# df2 = df1.groupby('playerID').sort_values('GP', ascending=False).join(dfPlayer)
# df2 = df1.groupby('playerID').sum().sort_values('GP', ascending=False).join(dfPlayer)
#print("Player: " + df2.iloc[0, 1] + " " + df2.iloc[0, 2] + "; GIDP: " + str(df2.iloc[0, 0]))