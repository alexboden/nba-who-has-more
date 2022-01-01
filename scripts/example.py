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


def games_with_x_or_more_points(seasons, x, player_id):
    count = 0

    for s in seasons:
        time.sleep(0.6)
        gamelog_player = playergamelog.PlayerGameLog(player_id = player_id, season = s)

        df_player_games = gamelog_player.get_data_frames()[0]

        box_scores_points = df_player_games.loc[:, "PTS"]

        for points in box_scores_points:
            if(points >= x):
                count += 1
    return count


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



all_time_great_list_file = open("NBA/alltimegreats.txt","r")

ALL_TIMERS = []

while(True):
    line = all_time_great_list_file.readline()[3:].strip()
    if not line:
        break
    ALL_TIMERS.append(line)

player1 = ALL_TIMERS[randint(0, 99)]
player2 = ALL_TIMERS[randint(0, 99)] 

print(player1)
print(player2)

while(player1 == player2):
    player2 = ALL_TIMERS[randint(0, 99)]

player1_id = get_player_id(player1)
player2_id = get_player_id(player2)

player1_seasons = get_player_seasons(player1_id)
player2_seasons = get_player_seasons(player2_id)


ready = input()
print(player1 + " has " + str(games_with_x_or_more_points(player1_seasons, 30, player1_id)) + " games with 30 or more points")

print(player2 + " has " +str( games_with_x_or_more_points(player2_seasons, 30, player2_id)) + " games with 30 or more points")



# career = playercareerstats.PlayerCareerStats(player_id=player['id'])
# career_df = career.get_data_frames()[0]

# df_player_games.to_csv(filename)



# nba_players = players.get_players()
# for p in celtics_players:
#     player_dict = [player for player in nba_players if player['full_name'] == p][0]

#     career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
#     career_df = career.get_data_frames()[0]
#     print(career_df)


# bron = player_info.available_seasons.get_dict()

# player_info = playercareerstats.career_totals_regular_season(per_mode36='totals', player_id=2544)




print("--- %s seconds ---" % (time.time() - start_time))