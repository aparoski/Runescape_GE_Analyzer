import pandas as pd
import numpy as np

import datetime
import time

import requests
from bs4 import BeautifulSoup as bs

import json

Runescape_Items = pd.read_csv("Runescape_Item_Names.csv")

def epochms_to_dt(ms):
    s = int(ms) / 1000.0
    
    date = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    return(date)
    
#crawl through Wiki API to gather historical price data as far back as 2008
    
ID_df_list = []

for i in Runescape_Items["Name_ID"]:
    
    req = requests.get('https://api.weirdgloop.org/exchange/history/rs/all?id=' + 
                       str(i).strip() + 
                       '&lang=en&compress=false')
    soup = bs(req.content, 'html.parser')
    
    timeout_count = 0
    
    while soup.find('h1') != None:
        time.sleep(60)
        timeout_count += 1
        req = requests.get('https://api.weirdgloop.org/exchange/history/rs/all?id=' + 
                       str(i).strip() + 
                       '&lang=en&compress=false')
        soup = bs(req.content, 'html.parser')
        print("timeout:", timeout_count) 
    
    try:
    
        df = pd.DataFrame(json.loads(soup.text)[str(i).strip()]).rename(columns = {"timestamp" : "date"})
    
    except:
        print(soup.text)
        print()
        print(soup)
        input()
    
    df["date"] = df["date"].map(lambda x: epochms_to_dt(x))
    
    df['date']= pd.to_datetime(df['date'])
    
    #df = df[df["date"] < datetime.datetime.strptime('2024-09-18', '%Y-%m-%d')]
    
    ID_df_list.append(df)

    print(i + " prices have been loaded")
    
GE_data_history = pd.concat(ID_df_list)

GE_data_history.to_csv("ID_Prices.csv")