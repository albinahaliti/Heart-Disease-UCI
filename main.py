import requests_html
import pandas as pd
import numpy as np
from pandas import DataFrame
df1=pd.read_csv("chol.csv")
df2=pd.read_csv("exang.csv")
df3=pd.read_csv("fbs.csv")
df4=pd.read_csv("restecg.csv")
df5=pd.read_csv("thalach.csv")
df6=pd.read_csv("trestbps.csv")

dataframes=[df2,df3,df4,df5,df6]
new=[]
for x in dataframes:
    x=x.set_index('Time')
    new.append(pd.Series(x.values.tolist(),index=x.index))
dataframe=pd.concat(new,axis=1,keys=('chol','exang','fbs','restecg','thalach','trestbps'),sort=True)
dataframe.to_csv("final_data.csv")
print(dataframe)