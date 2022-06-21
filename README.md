# Runescape_GE_Analyzer
## Tool to initially scrape Runescape 3 item IDs for tradeable items, use those IDs to gather price data daily, then run analysis on the gathered data. Tool consists of two halves: webscraping and analysis.

## General

Runescape is an online MMORPG, with many of the flavors of other games of its type. One of the more interesting components of the game is an exchange system, called the Grand Exchange. On the Grand Exchange players are able to trade items with other players using gold coins as a currency. Based on item supply and demand, prices fluctuate daily. I plan to examine price fluctuations in relation to game events such as double xp weekends, skill updates, game patches, etc...


## Webscraping

### Initial Item Information - script 1

Starting out, we do not have a list of all current Runescape 3 items that we may find on the game's grand exchange. To fill this list out, we can collect the list of tradeable item names from the runescape fandom website and then use those names to search the runescape grand exchange site for additional item information.

We will send the new information to our database. 

Once we have a starting list, this script can be run every once in a while to update the analyzer with new items added to the game, without the need for a manual check each time this happens. We can reduce proccessing time by shortening the list of item names used to check the grandexchange site by removing any items that have already been entered into the database. 

### Logged Item Scraper - script 2

Once we scrape the initial item information for most of the grand exchange items, we should be able to navigate to each item using their Item IDs or a scraped URL. Using these we can reduce the steps of scraping and minimize our interactions with the grand exchange website. We should only need to make one request per item to get information on current price. 

The information will be sent to the database. 

this script is set to run automatically each day at 06:00 UTC. 

### GE Historical data - script 3

The runescape wiki contains historical data which can be accessed via their API: https://runescape.wiki/w/Help:APIs
This code uses the API to collect all daily item prices from 2008 to today. 

## Analysis

Individual Analysis will be posted to the associated kaggle dataset: www.kaggle.com/dataset/a1ca952def9da4144f1a82279658e1c5608c3f79d5187eca206fd8f38db20fbc
