# Runescape_GE_Analyzer
## Tool to initially scrape Runescape 3 item IDs for tradeable items, use those IDs to gather price data daily, then run analysis on the gathered data. Tool consists of two halves: webscraping and analysis.



## Webscraping

### Initial Item Information - script 1

Starting out, we do not have a list of all current Runescape 3 items that we may find on the game's grand exchange. To fill this list out, we can collect the list of tradeable item names from the runescape fandom website and then use those names to search the runescape grand exchange site for additional item information.

We will send the new information to our database. 

Once we have a starting list, this script can be run every once in a while to update the analyzer with new items added to the game, without the need for a manual check each time this happens. We can reduce proccessing time by shortening the list of item names used to check the grandexchange site by removing any items that have already been entered into the database. 

### Logged Item Scraper - script 2

Once we scrape the initial item information for most of the grand exchange items, we should be able to navigate to each item using their Item IDs or a scraped URL. Using these we can reduce the steps of scraping and minimize our interactions with the grand exchange website. We should only need to make one request per item to get information on current price. 

The information will be sent to the database. 

this script is set to run automatically each day at 06:00 UTC. 
