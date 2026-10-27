from pydoc import describe

import seaborn as sns
import numpy as np
import pandas as pd

#df = sns.load_dataset('titanic')
#df.head()
#print(df.info())
#print(df['survived'].value_counts())
#print(df['alive'].value_counts()) # x
#print(df['embark_town'].value_counts())
#print(df['embarked'].value_counts()) # x
#print(df['pclass'].value_counts())
#print(df['class'].value_counts()) # x
#------------------------------------- first commit
#print(df.info())
#df1 = df.drop(['alive', 'class', 'embarked'], axis=1)
#print(df1.info())
#print(df1.groupby('sex')['survived'].mean())
#print(df1.groupby(['sex','pclass'])['survived'].mean())
#print(df1.groupby(['sex','pclass'])['survived'].agg(['mean','median','count']))
#print(df1.groupby(['sex','pclass'])[['survived','age']].agg({'survived':'mean', 'age':'median'}))
#--------------------------------------- second commit
#def get_IQR(data):
#    _3rd = data.quantile(.75)
#    _1st = data.quantile(.25)
#    return (np.abs(_3rd - _1st) * 1.5)

#print(df1.groupby(['sex','pclass'])['age'].apply(get_IQR))
#-------------------------------------- Third commit
#df2 = sns.load_dataset('penguins')
#print(df2.head())
#print(df2.info())
#print(df2.isna().sum())
#print(df2['species'].value_counts())
#print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())
#print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean())))
#df2 = df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))
#------------------------------------------ fourth commit
#df3 = pd.read_csv('APPL_price.csv')
#print(df3.head())
#print(df3.tail())
#print(df3.info())
#df3['Date'] = pd.to_datetime(df3['Date'])
#df3 = df3.set_index('Date')
#print(df3.head())
#print(df3['1980-12-12':'1980-12-18'])
#print(df3['2022-06':'2022-06'])
#print(df3.resample('7D').mean()) #7일 단위 평균/ 월을 원하면 D대신 ME 사용
#------------------------------------------ fifth commit
df4 = pd.read_csv('Uber.csv')
#print(df4.info())
#print(df4.head())
#print(df4.describe())
#print(df4.tail())
df4['START_DATE*'] = pd.to_datetime(df4['START_DATE*'], errors='coerce')
df4['END_DATE*'] = pd.to_datetime(df4['END_DATE*'], errors='coerce')
df4 = df4.sort_values(['START_DATE*','END_DATE*'])
print(df4.tail())
#print(df4['CATEGORY*'].value_counts())
#print(df4['START*'].value_counts())
#print(df4['STOP*'].value_counts())
print(df4.describe())
print(df4[df4['MILES*'] == df4['MILES*'].max()])
df4 = df4.drop(1155)
print(df4['MILES*'].describe())
df4['DURATION*'] = (df4['END_DATE*'] - df4['START_DATE*']).dt.total_seconds() / 60
print(df4.info())
print(df4.groupby(['CATEGORY*','PURPOSE*'])[['MILES*','DURATION*']].agg(['mean','std','count']))
#----------------------------------------------------final commit of today