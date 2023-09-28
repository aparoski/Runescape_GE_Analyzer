import pandas as pd
import numpy as np
import pyodbc

import datetime
import time

import requests
from bs4 import BeautifulSoup as bs

import json

#database stuff ---------------------------------------------------------------
conn = pyodbc.connect(r'Driver={SQL Server};'
                     r'Server=Helios;'
                     r'Database=Data_Science_Hangout;'
                     r'Trusted_Connection=yes;')

cursor = conn.cursor()

SQL = """SELECT U.NAME_ID, U.NAME_URL, N.NAME 
            FROM dbo.RUNESCAPE_ITEMS_URLS AS U 
            INNER JOIN dbo.RUNESCAPE_ITEMS_NAMES AS N 
                ON U.NAME_ID = N.NAME_ID"""

Runescape_Items = pd.read_sql_query(SQL, conn)

#database stuff ---------------------------------------------------------------

conn.close()

Runescape_Items = pd.read_csv("Runescape_Item_Names.csv")


def epochms_to_dt(ms):
    s = int(ms) / 1000.0
    
    date = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    return(date)
    


#crawl through Wiki API to gather historical price data as far back as 2008
    
ID_df_list = []

for i in Runescape_Items["NAME_ID"]:
    
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
    
    df = df[df["date"] < datetime.datetime.strptime('2022-06-11', '%Y-%m-%d')]
    
    ID_df_list.append(df)
    
GE_data_history = pd.concat(ID_df_list)

#database stuff ---------------------------------------------------------------



conn = pyodbc.connect(r'Driver={SQL Server};'
                     r'Server=Helios;'
                     r'Database=Data_Science_Hangout;'
                     r'Trusted_Connection=yes;')

cursor = conn.cursor()
    
for index, row in GE_data_history.iterrows():

    query = "INSERT INTO dbo.RUNESCAPE_ITEMS_PRICES (NAME_ID, Price, Date) VALUES ('{}', '{}', '{}')".format(row["id"],
                                                                                                             row["price"],
                                                                                                             row["date"])
    cursor.execute(query)

conn.commit()
conn.close()

#database stuff ---------------------------------------------------------------