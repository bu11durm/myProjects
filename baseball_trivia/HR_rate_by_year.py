import pandas as pd
from matplotlib import pyplot as plt
# need matplotlib import here

gcols = ['yearID', 'AB' ,'HR', 'BB', 'HBP', 'SH', 'SF']
df1 = pd.read_csv ('data\Batting.csv',
                   index_col=['yearID'], usecols=gcols)
df2 = df1.groupby('yearID').sum()
df2['HRRate'] = df2['HR'] / (df2['AB'] + df2.iloc[:, -4:-1].sum(axis=1))
print(df2.sort_values('HRRate', ascending=False).head(20))
# print(df2.dtypes)
# group into decades by removing the last digit of the year
df2['Decade'] = df2.index // 10
print(df2)
df3 = df2.groupby('Decade').mean()

# print(df3.dtypes)
# add decade back as the grouped number with a 0 appended
df3['Decade'] = df3.index * 10

df3.plot(kind='line',x='Decade',y='HRRate')
plt.show()


