import json
import requests
import requests_cache
import arrow
import subprocess
import os
from datetime import date

today = date.today()
def dateOfGames():
    url = 'https://api-web.nhle.com/v1/score/' + str(today)
    r = requests.get(url).json()
    # Check if 'gameWeek' key exists in the response
    if 'gameWeek' in r:
        for gameWeek in r['gameWeek']:
            date = gameWeek.get('date', '')
            dayAbbrev = gameWeek.get('dayAbbrev', '')
            numOfGames = gameWeek.get('numberOfGames', 0)
            # You can print or process the date, dayAbbrev, and numOfGames here
            print(f"Date: {date}, Day Abbreviation: {dayAbbrev}, Number of Games: {numOfGames}")
#dateOfGames()

def games():
    url = 'https://api-web.nhle.com/v1/score/' + str(today) 
    r = requests.get(url).json()
    if 'games' in r:
        for games in r['games']:
             if 'games' in r:
                for game in r['games']:
                    home_team_name = game.get('homeTeam', {}).get('abbrev')
                    home_team_logo = game.get('homeTeam', {}).get('logo')
                    away_team_name = game.get('awayTeam', {}).get('abbrev')
                    away_team_logo = game.get('awayTeam', {}).get('logo')
                    

                    print(f" {home_team_name} {home_team_logo} vs {away_team_name} {away_team_logo}")            
games()