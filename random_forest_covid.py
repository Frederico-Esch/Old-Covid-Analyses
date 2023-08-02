#%%
import pandas as pd 
import numpy as np 
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

#%%
brazil = pd.read_csv("brazil_data.csv")
Y = brazil.iloc[:, 7:8].values
X = brazil.iloc[:,1:2 ].values

#X vai ser novos casos, casos cumulativos e data
X = np.concatenate((X, brazil.iloc[:,5:6 ].values,brazil.iloc[:,6:7].values ), 1)

#após dia 26 de fevereiro
#Renomeando dias por indexes
for i in range(0,167):
    X[i][0] = i

#%%
regressor = RandomForestRegressor().fit(X,Y)
prediction = regressor.predict(X)
#%%
score = r2_score(Y,prediction)
plt.plot(X[:,0:1],Y, color="red", label = "data")
plt.plot(X[:,0:1],prediction, color="blue", label = "prediction")
plt.title(score)
plt.legend()
plt.show()
#%%
