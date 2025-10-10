import pandas as pd
import numpy as np 
df = pd.read_xls('crime_dataset_india.xls')
df.head()
df.info()
df2= df.dropna( axis=1)
df2.dtypes
df2["Date of Occurrence"] = pd.to_datetime(df2["Date of Occurrence"], format="mixed")
df2["Time of Occurrence"] = pd.to_datetime(df2["Time of Occurrence"], format = "mixed")
df2.dtypes