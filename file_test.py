import pandas as pd
import config


dir = config.upper_dir

loc_1 = "\\Runescape_GE_Analytics_2024-09-18\\"

loc_2 = "\\Runescape_GE_Analytics_2024-11-02\\"

file_name = "Runescape_Item_Prices.csv"

price_1 = pd.read_csv(dir + loc_1 + file_name)

price_2 = pd.read_csv(dir + loc_2 + file_name)

print(price_1.shape)
print()
print(price_2.shape)

print(price_2.shape[0] - price_1.shape[0])

print(price_1.id.drop_duplicates().shape[0] == price_2.id.drop_duplicates().shape[0])

print(price_1.date.drop_duplicates().shape[0] < price_2.date.drop_duplicates().shape[0])