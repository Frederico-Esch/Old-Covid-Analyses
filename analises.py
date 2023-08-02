#%%
import pandas as pd 
import numpy as np 
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#%%
brazil = pd.read_csv("brazil_data.csv")
Y = brazil.iloc[:, 7:8].values
X = brazil.iloc[:,1:2 ].values
#X vai ser novos casos, casos cumulativos e data
X = np.concatenate((X, brazil.iloc[:,5:6 ].values,brazil.iloc[:,6:7].values ), 1)


#%% após dia 26 de fevereiro
#Renomeando dias por indexes
for i in range(0,167):
    X[i][0] = i

#%%
regressor = LinearRegression().fit(X,Y)

#%%
plt.plot(X[:, 0:1],Y, c="red", label = "data")
plt.plot(X[:, 0:1],regressor.predict(X), c=(0,0,1), label = "prediction")
plt.legend()
plt.show()

#%%
#X = X[:,0:1]
trans2 = PolynomialFeatures(degree=2)
trans3 = PolynomialFeatures(degree=3)
trans4 = PolynomialFeatures(degree=4)
trans5 = PolynomialFeatures(degree=5)

X2 = trans2.fit_transform(X)
X3 = trans3.fit_transform(X)
X4 = trans4.fit_transform(X)
X5 = trans5.fit_transform(X)

Xs = [X2,X3,X4,X5]

regressor2 = LinearRegression().fit(X2, Y)
regressor3 = LinearRegression().fit(X3, Y)
regressor4 = LinearRegression().fit(X4, Y)
regressor5 = LinearRegression().fit(X5, Y)

regressors = [regressor2,regressor3,regressor4, regressor5]
#%%
plt.plot(X[:, 0:1],Y, c="red", label = "data")
plt.plot(X[:, 0:1],regressor.predict(X), c=(0,0,1), label = "linear")
plt.plot(X[:, 0:1],regressor2.predict(X2), c=(0,.7,0.7), label = "Poly 2")
plt.plot(X[:, 0:1],regressor3.predict(X3), c=(1,0,1), label = "Poly 3")
plt.plot(X[:, 0:1],regressor4.predict(X4), c=(1,1,0), label = "Poly 4")
plt.plot(X[:, 0:1],regressor5.predict(X5), c=(0,0.6,0), label = "Poly 5")
plt.legend()
plt.show()


#%%
score = r2_score(Y,regressor.predict(X))
score2 = r2_score(Y,regressor2.predict(X2))
score3 = r2_score(Y,regressor3.predict(X3))
score4 = r2_score(Y,regressor4.predict(X4))
score5 = r2_score(Y,regressor5.predict(X5))
scores = []
scores.append(score)
scores.append(score2)
scores.append(score3)
scores.append(score4)
scores.append(score5)
for i in range(0,5):
    print(f"Poly {i+1}: {scores[i]}")
#%%
for i in range(0,4):
    plt.plot(X[:, 0:1],Y, c="red", label = "data")
    plt.plot(X[:, 0:1],regressors[i].predict(Xs[i]), c=(0,0,.7), label = f"Poly {i+2}")
    plt.title(f"adjusted r^2: {scores[i+1]}")
    plt.legend()
    plt.show()