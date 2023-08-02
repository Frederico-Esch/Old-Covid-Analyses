#%%
import pandas as pd 
import numpy as np 
#%%
datag = pd.read_csv("WHO-COVID-19-global-data.csv")
#%%
brazil= datag.iloc[4221:4388,:]
#%%
brazil.to_csv("brazil_data.csv")