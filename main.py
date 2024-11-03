import GE_Historical_Data
import gen_funcs
import metadatajson
import shutil

#perform directory operations
#make new data folder
Previous_data_loc = gen_funcs.most_recent_local_dataset()
gen_funcs.make_new_recent_folder()

#maybe keep functions separate in case I want to access latest set w/o creating one
data_dump_loc = gen_funcs.most_recent_local_dataset()
print(data_dump_loc)


#perform data scraping
GE_Historical_Data.rune_wiki_api_crawler(data_dump_loc + "//Runescape_Item_Prices.csv")

#place all files in folder

shutil.copyfile(Previous_data_loc + "//Runescape_Item_Names.csv"
                , data_dump_loc + "//Runescape_Item_Names.csv")
shutil.copyfile(Previous_data_loc + "//Runescape_Item_URLS.csv" 
                , data_dump_loc + "//Runescape_Item_URLS.csv")

#generate meta data json for folder

metadatajson.write_rs_JSON(data_dump_loc + "//metadata.json")

#connect to kaggle through API and upload dataset