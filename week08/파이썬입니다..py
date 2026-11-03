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