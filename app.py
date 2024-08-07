import pandas as pd

trackers = ["Previous Point Trackers (2020-24)/SPRING 2022 BOARD POINT TRACKER.csv",
            "Previous Point Trackers (2020-24)/FALL 2022_ CSF POINT TRACKER.csv",
            "Previous Point Trackers (2020-24)/SPRING 2023_ CSF POINT TRACKER.csv",
            "Previous Point Trackers (2020-24)/FALL 2023 - CSF Point Tracker.csv",
            "Previous Point Trackers (2020-24)/SPRING 2024 - CSF Point Tracker (1).csv"]

years = [1,2,2,3,3]


data = {}

for tracker in trackers:
    dataframe = pd.read_csv(tracker,keep_default_na=False)
    print(dataframe)

    for index,row in dataframe.iterrows():
        key = f"{str(row[0]).lower().strip()} {str(row[1]).lower().strip()}"
        if(row["point13"].strip() != ""):
            if(key in data):
                data[key][trackers.index(tracker)]=True
            else:
                data[key] = [False]*len(trackers)
                data[key][trackers.index(tracker)]=True
                data[key].append(years[trackers.index(tracker)]-int(row["GRADE:"].strip().removesuffix("th"))+33)
        

newData = {}
for key,val in data.items():
    newData[key]=tuple(val)

df = pd.DataFrame.from_dict(newData)

df.transpose().to_csv('results.csv')