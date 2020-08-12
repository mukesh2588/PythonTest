import pandas as pd
import numpy as np
x = pd.Series()
print(x)
numarr=np.array(['a','b','c','d'])
s=pd.Series(numarr)
print(s)

dictarr={'x':0,'y':1,'z':5}
s=pd.Series(dictarr)
print(s)

data=[['Siju','10'],['kamalini',20],['prashanth',78]]
df=pd.DataFrame(data,columns=['Name','Score'])
print(df)