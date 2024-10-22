import json
import os

my_dir = os.path.dirname(__file__)

#gather current metadata for dataset names and descriptions
meta_data_runescape = "runescape-grand-exchange-data-metadata.json"
with open(my_dir + "\\" + meta_data_runescape, mode = "r", encoding = "utf-8") as read_file:
    rune_meta = json.load(read_file)

#set up the bits which will go to generating the metadata file
#note to self - update the name field to pick up name directly from python dataframe
title = "Runescape Grand Exchange Data"
subtitle = rune_meta["alternateName"]
description = rune_meta["description"]
id = "aparoski/runescape-grand-exchange-data"
licenses = rune_meta["license"]

Names_Path = rune_meta["distribution"][1]["contentUrl"]
Names_Desc = rune_meta["distribution"][1]["description"]
Names_Fields = [{"name" : "Name_ID", 
                 "title" : "a unique identifier for an item", 
                 "type" : "id"},
                 {"name" : "Name",
                  "title" : "the item's in-game name",
                  "type" : "string"}]


Price_Path = rune_meta["distribution"][2]["contentUrl"]
Price_Desc = rune_meta["distribution"][2]["description"]
Price_Fields =[{"name" : "id",
                "title" : "an item's unique reference ID",
                "type" : "id"},
                {"name" : "price",
                 "title" : "The average amount of coins an item has traded for on a particular date",
                 "type" : "integer"}]

URL_Path = rune_meta["distribution"][3]["contentUrl"]
URL_Desc = rune_meta["distribution"][3]["description"]
URL_Fields = [{"name" : "Name_ID",
               "title" : "Unique ID given to an item",
               "type" : "id"},
               {"name" : "Name_URL",
                "title" : "Runescape's Grand Exchange website URL for the Associated item",
                "type" : "string"}]

#combine bits into JSON file
new_RS_JSON = {
                "title" : title,
                "subtitle" : subtitle,
                "description" : description,
                "id" : id,
                "licenses" : licenses,
                "resources" : [
                                {
                                    "path" : Names_Path,
                                    "description" : Names_Desc,
                                    "schema" : {
                                                "fields" : Names_Fields
                                    }
                                },
                                {
                                    "path" : Price_Path,
                                    "description" : Price_Desc,
                                    "schema" : {
                                                "fields" : Price_Fields
                                    }

                                },
                                {
                                    "path" : URL_Path,
                                    "description" : URL_Desc,
                                    "schema" : {
                                                "fields" : URL_Fields
                                    }

                                }
                                ]
                }

print(new_RS_JSON)