import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/" #-> 웹사이트 주소로 가져갈 수 있음! 직접 사이트 들어가서 가져오는 것도 가능!
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values
#print(lifesat)
#df_x = pd.DataFrame(X, columns=["GDP per capita (USD)"])
#print(df_x.head())
#--------------------------------- first commit


# Visualize the data
lifesat.plot(kind='scatter', grid=True,
x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_000, 62_500, 3, 9])
plt.show()
#Select a linear model
#model = LinearRegression()
# Train the model
#model.fit(X, y)
# Make a prediction for Cyprus
#X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
#print(model.predict(X_new)) # output: [[6.30165767]]
