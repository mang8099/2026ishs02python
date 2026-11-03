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
df = pd.read_csv('German_credit.csv')
#print(df.head())
#print(df.info())
#print(df['Age'].describe())
#print(pd.cut(df['Age'], bins=8))
#print(pd.cut(df['Age'], bins=8).reset_index().groupby('Age').size())
ages = [10, 20, 30, 40, 50, 60, 70, 80]
print(pd.cut(df['Age'], bins=ages))
print(pd.cut(df['Age'], bins=ages, right=False))
print(pd.cut(df['Age'], bins=ages).reset_index().groupby('Age').size())