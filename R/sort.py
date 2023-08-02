#%%
import pandas as pd
import numpy as np
#%%
brazil = pd.read_csv("brazil_data.csv")

brazil = brazil.iloc[:,1:].values

brazil = brazil[:,4:8]
brazil_data = pd.DataFrame(brazil,columns= [ "NC", "C", "NM", "M"])
#%%
brazil_data.to_csv("brazil_data.csv")
