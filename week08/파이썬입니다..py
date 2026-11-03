import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd
import numpy as np

#df4 = pd.read_csv('Uber.csv')
#df4['START_DATE*'] = pd.to_datetime(df4['START_DATE*'], errors='coerce')
#df4['END_DATE*'] = pd.to_datetime(df4['END_DATE*'], errors='coerce')
#df4 = df4.sort_values(['START_DATE*', 'END_DATE*'])
#df4 = df4.drop(1155)
#df4['DURATION*'] = (df4['END_DATE*'] - df4['START_DATE*']).dt.total_seconds() / 60
#df4 = df4.dropna()
#slope, intercept, relation, _, _ = linregress(df4['MILES*'], df4['DURATION*'])

#fig, ax = plt.subplots()
#sns.regplot(x='MILES*', y='DURATION*', data=df4, ax=ax,
 #           line_kws={'label': f'y={slope:.2f}x+{intercept:.2f}, R^2={relation**2:.2f}'})
#plt.legend()
#plt.show()
#---------------------------------- teacher's first commit
#df = pd.read_csv('German_credit.csv')
#print(df.head())
#print(df.info())
#print(df['Age'].describe())
#print(pd.cut(df['Age'], bins=8))
#print(pd.cut(df['Age'], bins=8).reset_index().groupby('Age').size())
#ages = [10, 20, 30, 40, 50, 60, 70, 80]
#print(pd.cut(df['Age'], bins=ages))
#print(pd.cut(df['Age'], bins=ages, right=False))
#print(pd.cut(df['Age'], bins=ages).reset_index().groupby('Age').size())
#print(pd.qcut(df['Age'], q=8))
#print(pd.qcut(df['Age'], q=8, duplicates='drop').reset_index().groupby('Age').size()) #qcut은 백분율로 나눔
#________________________________________ teacher's second commit
#s = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 1, 0])
#sc = s.cumsum()
#print(sc)
#print(s.mul(sc))
#print(s.mul(sc).diff())
#print(s.mul(sc).diff().where(lambda n: n < 0))
#print(s.mul(sc).diff().where(lambda n: n<0).ffill()) #ffill은 앞에 값을 가져가고, bfill은 뒤에 값을 가져감
#print(s.mul(sc).diff().where(lambda n: n<0).ffill().add(sc, fill_value=0))
#print(s.mul(sc).diff().where(lambda n: n<0).ffill().add(sc, fill_value=0).max())
#------------------------------------------ teacher's third commit
#df = pd.read_csv('APPL_price.csv')
#s = df['Close'] > 175
#print(df[s])
#sc = s.cumsum()
#print(s.mul(sc).diff().where(lambda x: x<0).ffill().add(sc, fill_value=0).max()) # max함수와 min함수는 연속된 개수에 대한 것임
#------------------------------------------------
df = pd.read_csv('weight_height.csv')
print(df.describe())
print(df.info())
#sns.scatterplot(x="Weight", y="Height", data=df)
#plt.show()
print(df.sort_values(by = 'Weight', ascending = False))
criteria = df['Weight'].quantile(0.9999)
df_new = df[df['Weight'] < criteria]
sns.scatterplot(x='Weight', y='Height', data=df_new)
plt.show()
print(df[df['Weight'] > 390].index)
print(df.iloc[2014])
df['Weight'] = df['Weight'].clip(70, 300)
print(df.iloc[2014])
