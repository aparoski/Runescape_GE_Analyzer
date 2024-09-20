import pandas as pd

prices = pd.read_csv("ID_Prices.csv")

print(prices[prices["id"] == 44828])

prices.to_csv("A:\Data_Science\Projects\Runescape_GE_Tracker\Data_Store\Runescape_GE_Analytics_2024-09-18\Runescape_Item_Prices.csv")