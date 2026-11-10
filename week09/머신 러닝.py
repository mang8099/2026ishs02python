import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

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
#model = LinearRegression() -> 선형회귀
model = KNeighborsRegressor(n_neighbors=3) # -> K-NN 회귀(최근접 이웃 모델) n_neighbors = 3 이므로 x값이 근접한 3개의 이웃의 y값을 평균냄
# Train the model
model.fit(X, y)
# Make a prediction for Cyprus
X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # 선형회귀: [[6.30165767]] 최근점 이웃 모델 : [[6.33333333]]

X_new1 = [[33_645.77]] #한국의 GPD
print(model.predict(X_new1)) # 선형외귀 : [[6.0298~~]] 최근접 이웃 모댈 : [[5.7333333333]]
