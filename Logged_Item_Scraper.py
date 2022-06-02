import pandas as pd
import numpy as np
import pyodbc

import datetime
import time

import requests
from bs4 import BeautifulSoup as bs


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

SQL = """SELECT * FROM RUNESCAPE_ITEMS_PRICES"""
#checking current contents of the database
Past_Prices = pd.read_sql_query(SQL, conn)

conn.close()
#database stuff ---------------------------------------------------------------

#webscraping ------------------------------------------------------------------
prices = []
for index, row in Runescape_Items.iterrows():
    req = requests.get(str(row["NAME_URL"]).strip())
    soup = bs(req.content, 'html.parser')
    
    while soup.find('div', {'class' : 'content error'}) != None:
        time.sleep(360)
        req = requests.get(str(row["NAME_URL"]).strip())
        soup = bs(req.content, 'html.parser')
        

    for i in soup.find_all("h3"):
        print(row["NAME"], i)
        if "Current Guide Price" in i.get_text():
            price = i.find("span").get('title').replace(",", "")
            break
    prices.append([row["NAME"], row["NAME_ID"], price, datetime.date.today()])
#webscraping ------------------------------------------------------------------
    
#dataframe stuff --------------------------------------------------------------
price_df = pd.DataFrame(prices, columns = ["NAME", "NAME_ID", "Price", "Date"])

price_df = price_df.astype({"NAME" : 'string', "Date" : "datetime64[ns]"})

#perform right antijoin to collect any price updates that have not yet been
#entered into the database
to_database = Past_Prices.merge(price_df, on = ["NAME_ID", "Date"], how = 'outer', indicator = True)
to_database = to_database[to_database._merge == 'right_only'].drop("_merge", axis = 1)

#dataframe stuff --------------------------------------------------------------

if to_database.shape[0] > 0:
    

    #database stuff ---------------------------------------------------------------
    
    conn = pyodbc.connect(r'Driver={SQL Server};'
                         r'Server=Helios;'
                         r'Database=Data_Science_Hangout;'
                         r'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
        
    for index, row in to_database.iterrows():
    
        query = "INSERT INTO dbo.RUNESCAPE_ITEMS_PRICES (NAME_ID, Price, Date) VALUES ('{}', '{}', '{}')".format(row["NAME_ID"],
                                                                                                                 row["Price_y"],
                                                                                                                 row["Date"])
        
        print(query)
        
    
        cursor.execute(query)
    
    conn.commit()
    conn.close()
    
    #database stuff ---------------------------------------------------------------
    
else:
    print("No prices to update")
