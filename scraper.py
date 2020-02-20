##IMPORTS##
import requests
from bs4 import BeautifulSoup as bs
import re
import pyodbc
import pandas as pd

##DATABASE CONNECTION##
#1 establish connection to the database
#2 create a cursor (which facilitates db transactions)
cnxn = pyodbc.connect('DSN=NFLStats;') # This requires valid database connection via DNS. 
crsr = cnxn.cursor()

##SCRAPE##
##Scrape Team Names##
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
r = requests.get('https://pro-football-reference.com/teams/')
page = bs(r.text, 'html.parser')\

team_dict = {}

for link in page.find_all('a', attrs={'href': re.compile("^/teams/")}):
    if link.string.find(" ") > 0: # this returns a set of just team names and city + team names, this filters to just city + names
        team_dict[link.string] = link.get('href')[7:10]
#print(team_dict)


##Scrape Box Scores##
#After testing 1 week and season, create a nested for loop and do all the weeks and seasons!!
season = '2019' 
week = '1'

r = requests.get(f'https://www.pro-football-reference.com/years/{season}/week_{week}.htm')
page = bs(r.text, 'html.parser')
#print(page)

for link in page.find_all(href=re.compile(f"boxscores/{season}")):
    print(link)




