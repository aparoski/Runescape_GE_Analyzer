import json
import os

my_dir = os.path.dirname(__file__)

meta_data_runescape = "runescape-grand-exchange-data-metadata.json"

with open(my_dir + "\\" + meta_data_runescape, mode = "r", encoding = "utf-8") as read_file:
    rune_meta = json.load(read_file)

title = "Runescape Grand Exchange Data"

subtitle = rune_meta["alternateName"]

id = "aparoski/runescape-grand-exchange-data"

Names_Path = rune_meta["distribution"][1]["contentUrl"]
Names_Desc = rune_meta["distribution"][1]["description"]
Names_Fields = [{"name" : "Name_ID", 
                 "description" : "a unique identifier for an item", 
                 "type" : "id"},
                 {"name" : "Name",
                  "description" : "the item's in-game name",
                  "type" : "string"}]


Price_Path = rune_meta["distribution"][2]["contentUrl"]
Price_Desc = rune_meta["distribution"][2]["description"]
Price_Fields

URL_Path = rune_meta["distribution"][3]["contentUrl"]
URL_Desc = rune_meta["distribution"][3]["description"]

print(Names_Desc)