import pandas as pd
import numpy as np

from selenium import webdriver
from bs4 import BeautifulSoup

import time
import datetime

import re
from itertools import permutations


driver = webdriver.Chrome(r"A:\Data Science\Programming\Webdrivers\chromedriver_101.exe") #replace with the up to date version of chrome driver
driver.get("https://runescape.fandom.com/wiki/Category:Tradeable_items")

#extract all tradeable item names from the runescape wiki

item_names = []

while len(driver.find_elements_by_css_selector("a.category-page__pagination-next.wds-button.wds-is-secondary")) > 0:

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    item_cats = soup.find_all("div", {"class" : "category-page__members-wrapper"})
    
    for i in item_cats:
        print(i.find('div').text)
        items = i.find_all("a", {"class" : "category-page__member-link"})
        for j in items:
            item_names.append(j.text)
            
    time.sleep(2.5)
    try:
        next_page = driver.find_element_by_css_selector("a.category-page__pagination-next.wds-button.wds-is-secondary")
        next_page.click()
        
        #print(len(soup.find_all("a", {"class" : "category-page__pagination-next wds-button wds-is-secondary"})))
        
    except:
        
        print("failed_1")
        time.sleep(10)
        next_page = driver.find_element_by_css_selector("a.category-page__pagination-next.wds-button.wds-is-secondary")
        next_page.click()
        

def GE_Scrape(name):
    """ Returns the item URL as well as its current market price as of today's date"""
    

    
    driver.get('https://secure.runescape.com/m=itemdb_rs/')
    
    #clear the cookies window
    
    if len(driver.find_elements_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')) > 0:
        driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    while soup.find('div', {'class' : 'content error'}) != None:
        time.sleep(360)
        driver.get('https://secure.runescape.com/m=itemdb_rs/')
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
    

    driver.find_element_by_css_selector('input#item-search.text').send_keys(name)
    driver.find_element_by_css_selector('input.search-submit').click()
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    if soup.find('div', {'class' : 'content error'}) != None:
        error_counter = 0
        while soup.find('div', {'class' : 'content error'}) != None:
            print("IP Block", error_counter, name)
            time.sleep(360)
            driver.get('https://secure.runescape.com/m=itemdb_rs/')
            driver.find_element_by_css_selector('input#item-search.text').send_keys(name)
            driver.find_element_by_css_selector('input.search-submit').click()
            
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')
            
            error_counter += 1
    
        
    
    if "did not return any results" in soup.find('p').text:
        print(name, "was not found in ge database")
        return([-50, -50, datetime.datetime.strptime('9999-12-01', '%Y-%m-%d')])
    
    def word_caps(word):
            """function returns a list of all combinations of first letter capitalizations
            from a string of words"""

            word_list = word.split()

            cap_words = [i.capitalize() for i in word_list]

            low_words = [i.lower() for i in word_list]

            listed_perms = list(permutations(list(np.zeros(4, np.int8)) + list(np.ones(4, np.int8))))

            trimmed_perms = list(set([i[0 : -(8 - len(word_list))] for i in listed_perms]))

            zipped_words = list(zip(cap_words, low_words))

            sentences = []

            for i in trimmed_perms:
                sentences.append([zipped_words[j][i[j]] for j in range(len(i))])
                
            sentences_fin = [" ".join(i) for i in sentences]

            return(sentences_fin)
        
    #we use different forms of title case here because some terms from the runescape fandom website
    #may have incorrect capitalizations which will return incorrect results on the GE website.

    
    for i in word_caps(name):
        for j in driver.find_elements_by_class_name("table-item-link"):
            if i == j.get_attribute('title'):
                
                j.click()
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                
                while soup.find('div', {'class' : 'content error'}) != None:
                    time.sleep(360)
                    driver.execute_script("window.history.go(-1)")
                    
                    for k in driver.find_elements_by_class_name("table-item-link"):
                        if i == k.get_attribute('title'):
                    
                            k.click()
                            html = driver.page_source
                            soup = BeautifulSoup(html,'html.parser')
                            break
                    
                
                try:         
                    for i in soup.find_all('h3'):
                        if "Current Guide Price " in i.get_text():
                            result_1 = re.search('title="(.*)"', str(i.find('span')))
                            result_2 = driver.current_url
                            today = datetime.date.today()
                            print(name)
                            return([int(result_1.group(1).replace(",", "")), result_2, today])
                except: 
                    print("error at item page")
                    return([-100, -100, datetime.datetime.strptime('9999-12-01', '%Y-%m-%d')]) 
        
        
    print(name, "general failure")
    return([-100, -100, datetime.datetime.strptime('9999-12-01', '%Y-%m-%d')])           

#cheking our list of item names against what is already in our database
#to reduce redundancy
item_names_update = [i for i in item_names if i not in Runescape_Items["Name"]]           
    
if len(item_names_update) != 0:
    print("New items found")
    item_data = [GE_Scrape(i) for i in item_names_update]
    
    
    to_database = pd.DataFrame(item_data, columns = ["Price", "URL", "Date"])
    #extract item ID from the URL. Use as primary key in database
    to_database["Name_ID"] = to_database["URL"].map(lambda x: re.search('[0-9]*$', x).group(0) if isinstance(x, str) else str(x))
    to_database["Name"] = item_names_update
    #transform any apostrophes in the item names so that they can be entered into the database
    to_database["Name_db"] = to_database["Name"].map(lambda x: x.replace("'", "''"))
    
    
else:
    print("No new items")