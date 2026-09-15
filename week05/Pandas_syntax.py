import pandas as pd
import numpy as np

df = pd.read_csv('bike.csv')
#print(df.iloc[5:8, [0,5,7]])
#print(df.loc[5:7, ['datetime', 'temp', 'humidity']])
#print(df[df['season']==4]) #4/4분기
print(df.select_dtypes(exclude='int')) #int 제외 모든 타입 가지고 오기
df = df.set_index('datetime') #index를 datetime으로 설젇
print(df.filter(like='00:00:00', axis=0))
print(df.filter(items=['weather', 'count']))
print(df.filter(regex='p..d'))
print(df.filter(regex='day'))