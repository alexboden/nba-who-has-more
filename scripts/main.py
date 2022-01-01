import pandas as pd
from random import *

stat_combos = [
    [40, 'PTS', 'points'],
    [30, 'PTS', 'points'],
    [20, 'PTS', 'points'],
    [15, 'REB', 'rebounds'],
    [10, 'REB', 'rebounds'],
    [10, 'AST', 'assists'],
    [5, 'AST', 'assists'],
    [3, 'STL', 'steals'],
    [3, 'BLK', 'blocks']
]

def get_games_with_x_stat(player_df, x, stat):
    count = 0
    for points in getattr(player_df, stat):
        if(points >= x):
            count += 1
    
    return count

all_time_great_list_file = open("/Users/Alex/Documents/github/nba-who-has-more/scripts/alltimegreats.txt","r")

ALL_TIMERS = []

while(True):
    line = all_time_great_list_file.readline()[3:].strip()
    if not line:
        break
    ALL_TIMERS.append(line)

score = 0

while(True):

    player1 = ALL_TIMERS[randint(0, 99)]
    player2 = ALL_TIMERS[randint(0, 99)] 

    while(player1 == player2):
        player2 = ALL_TIMERS[randint(0, 99)]

    player1_df = pd.read_csv("/Users/Alex/Documents/github/nba-who-has-more/gamelogs/" + player1 + ".csv") 
    player2_df = pd.read_csv("/Users/Alex/Documents/github/nba-who-has-more/gamelogs/" + player2 + ".csv") 

    stat = stat_combos[randint(0, len(stat_combos) - 1)]

    print("\nWho has more regular season games with " + str(stat[0]) + " or more " + stat[2] + "?")

    print("1: " + player1)
    print("2: " +  player2)

    guess = input()
    while(guess != "1" and guess != "2"):
        guess = input("Invalid Input. Please enter 1 or 2:")

    print(player1 + " : " + str(get_games_with_x_stat(player1_df, stat[0], stat[1])))
    print(player2 + " : " + str(get_games_with_x_stat(player2_df, stat[0], stat[1])))
    
    if(int(get_games_with_x_stat(player1_df, stat[0], stat[1])) > int(get_games_with_x_stat(player2_df, stat[0], stat[1]))):
        if(guess == "1"):
            print("correct")
            score += 1
        else:
            break
    
    else:
        if(guess == "2"):
            print("correct")
            score += 1
        
        else:
            break

print("Incorrect")

print("Total Score : " + str(score))


