# File used to get all the games logs for all the players in the 'alltimegreats.txt' file

from nba_api.stats.static import players
from nba_api.stats import endpoints
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playergamelog

import pandas as pd
import time
from random import *
import time
start_time = time.time()

#list of all players
player_dict = players.get_players()


def get_game_logs(seasons, player_id, player_fullname):
    list_of_dfs = []
    for s in seasons:
        time.sleep(0.6)
        gamelog_player = playergamelog.PlayerGameLog(player_id = player_id, season = s)
        df_player_games = gamelog_player.get_data_frames()[0]
        list_of_dfs.append(df_player_games)

    final = pd.concat(list_of_dfs, axis=0)
    final.reset_index(inplace=True)
    final.to_json("alltimegreatgamelogs-json/" + player_fullname + ".json")
        
def get_player_id(fullname):
    player = [player for player in player_dict if player['full_name'] == fullname][0]
    return player['id']    


def get_player_seasons(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)

    available_seasons = player_info.available_seasons.get_dict()

    seasons = []

    for season in available_seasons["data"]:
        for s in season:
            year = s[1:5];
            if not year in seasons:
                seasons.append(year)

    return seasons



all_time_great_list_file = open("orginal-python/alltimegreats.txt","r")

ALL_TIMERS = []

while(True):
    line = all_time_great_list_file.readline()[3:].strip()
    if not line:
        break
    ALL_TIMERS.append(line)


for player in ALL_TIMERS:
    print("Getting player: " + player)
    player_id = get_player_id(player)
    player_seasons = get_player_seasons(player_id)
    get_game_logs(player_seasons, player_id, player)
    print("Done")

print("--- %s seconds ---" % (time.time() - start_time))