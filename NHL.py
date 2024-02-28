import pandas as pd
import datetime
from random import randint
from time import sleep
import os

url = "https://www.hockey-reference.com/leagues/NHL_2024.html"
dfs=pd.read_html(url)
df = dfs[0]
df.drop([0, 9], inplace=True)
columns =list(df.columns)
df.rename(columns= {'Unnamed: 0': 'Team Names'}, inplace=True)

#Get standings for eastern conference by points(Most points is #1)
sortByWinsEC = df.sort_values(by='PTS', ascending=False)
#print(sortByWinsEC)

#Get standings for western conference by points
df2 = dfs[1]
df2.drop([0,9], inplace=True)
sortByWinsWC = df2.sort_values(by='PTS', ascending=False)
#print(sortByWinsWC)

json = pd.read_json('https://api-web.nhle.com/v1/schedule/2024-02-09')
jsonTail= json.tail(6)
print(jsonTail)