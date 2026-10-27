import seaborn as sns
import numpy as np
import pandas as pd

df = sns.load_dataset('titanic')
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
df1 = df.drop(['alive', 'class', 'embarked'], axis=1)
#print(df1.info())
#print(df1.groupby('sex')['survived'].mean())
#print(df1.groupby(['sex','pclass'])['survived'].mean())
#print(df1.groupby(['sex','pclass'])['survived'].agg(['mean','median','count']))
#print(df1.groupby(['sex','pclass'])[['survived','age']].agg({'survived':'mean', 'age':'median'}))
#--------------------------------------- second commit
def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

print(df1.groupby(['sex','pclass'])['age'].apply(get_IQR))
#-------------------------------------- Third commit
df2 = sns.load_dataset('penguins')
#print(df2.head())
#print(df2.info())
#print(df2.isna().sum())
#print(df2['species'].value_counts())
#print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())
#print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean())))
#df2 = df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))
