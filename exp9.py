import pandas as pd
data=pd.read_csv("D:\\auto-mpg.CSV")
print(data)
cyclinder=data[data['cyclinder']==8]
print(cyclinder)
year=data.groupby("modelyear").size()
print(year)
