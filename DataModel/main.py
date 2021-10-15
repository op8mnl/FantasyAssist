#**************************************************************************************************************
# NBA-StatModel
# Date : 5/4/2021
# Authors : Felix Zheng | Jason Chen
# Version : 0.1 
#**************************************************************************************************************
# This program aims to scrape player statistics from the nba_api and create a fantasy basketball valuation
# of players in the league
#**************************************************************************************************************
#  libraries used: 
# | pandas | requests | numpy | nba_api | matplotlib | regex |
#
# Api usage: https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md
#
#**************************************************************************************************************

# importing the regular expressions library that is prebuilt into python to do string searches 
# basic information and usage https://www.w3schools.com/python/python_regex.asp
import re 
import pandas as pd
import sys
from nba_api.stats.static import players 
from nba_api.stats.endpoints import commonplayerinfo as cpi
from nba_api.stats.endpoints import playergamelog as pgl

# here we want a dictionary containing the active playerbase in the NBA
# the active_players dictionary is sorted aphabetically by last name

active_players = pd.DataFrame(players.get_active_players())

# Search function

player = sys.argv[1]
for i in range(len(active_players)):
    if(active_players['full_name'][i] == player):
        id = active_players['id'][i]
    
player_basicInfo = cpi.CommonPlayerInfo(id).get_data_frames()
player_statsInfo = pgl.PlayerGameLog(id).get_data_frames()
print(player_basicInfo[0]['FIRST_NAME'][0], player_basicInfo[0]['LAST_NAME'][0])
print(player_statsInfo)
sys.stdout.flush()



    
