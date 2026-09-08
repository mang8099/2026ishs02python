import numpy as np
import pandas as pd

array = np.array([[4,7,10], [5,8,11], [6,9,12]])
df = pd.DataFrame(array, columns = ['a', 'b', 'c'], index = [1,2,3])
print(df)
print(df.melt().rename(columns={'variable':'var', 'value':'val'}).query('val <= 7').sort_values(by=['val'], ascending=False).head(3))
#print(df.sort_values('mpg'))-- #seaborn
