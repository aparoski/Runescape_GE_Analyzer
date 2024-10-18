import json
import os

my_dir = os.path.dirname(__file__)

meta_data_runescape = "runescape-grand-exchange-data-metadata.json"

with open(my_dir + "\\" + meta_data_runescape, mode = "r", encoding = "utf-8") as read_file:
    rune_meta = json.load(read_file)

subtitle = rune_meta["alternateName"]

print(subtitle)