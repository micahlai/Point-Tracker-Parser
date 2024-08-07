import pandas as pd

directory = 'Previous Point Trackers (2020-24)/FALL 2022_ CSF POINT TRACKER.csv'

data = {}

dataframe = pd.read_csv(directory,keep_default_na=False)
#print(dataframe)

for index,row in dataframe.iterrows():
    data[f"{row[0]} {row[1]}"] = (row[15] != "")

print(data)