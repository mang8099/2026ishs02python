import numpy as np
import pandas as pd

array = np.array([[86,90,64,97], [29,100,76,96], [112,32,142,95]])
df = pd.DataFrame(array, columns = ['a', 'b', 'c','d'], index = [1,2,3])
print(df)
print(df.melt().rename(columns={'variable':'var', 'value':'val'}).query('val <= 50').sort_values(by=['val'], ascending=False).head(3))
#print(df.sort_values('mpg'))-- #seaborn
df1 = pd.DataFrame(array, columns = ['Kor', 'Eng', 'Math', 'Cs'], index = [1,2,3])
print(df1)
print(df1.iloc[1:, 2:])
print(df1.iloc[:, [1,3]])
print(df1.iloc[:, [0,1]])
print(df1.loc[:, ['Math', 'Cs']])
print(df1.loc[2:3, 'Math':'Cs'])
print(df1.iat[2,1])
print(df1.at[3,'Eng'])