import json
import requests
import requests_cache
import os
from datetime import date

today = date.today()

def games():
    games_list = []
    url = 'https://api-web.nhle.com/v1/score/' + str(today) 
    r = requests.get(url).json()
    if 'games' in r:
        for game in r['games']:
            game_date = game.get('gameDate', {})
            home_team_name = game.get('homeTeam', {}).get('abbrev')
            home_team_score = game.get('homeTeam', {}).get('score')
            home_team_logo = game.get('homeTeam', {}).get('logo')
            away_team_name = game.get('awayTeam', {}).get('abbrev')
            away_team_score = game.get('awayTeam', {}).get('score')
            away_team_logo = game.get('awayTeam', {}).get('logo')
            game_state = game.get('gameState', {})
            games_list.append({
                'game_date': game_date,
                'home_team_name': home_team_name + " vs " + away_team_name,             
                'Game state' : game_state,
                'Score' : str(home_team_score) + " - " + str(away_team_score),
            })
    
    return games_list

def top_3_players():
    url = 'https://api-web.nhle.com/v1/skater-stats-leaders/20232024/2?categories=points&limit=3'
    r= requests.get(url).json()
    top_3_playersl = []
    if 'points' in r:
        for player in r['points']:
            player_firstname = player.get('firstName', {}).get('default')
            player_lastname = player.get('lastName', {}).get('default')
            points = player.get('value', {})
            player_picture = player.get('headshot', {})
            player_name = f"{player_firstname} {player_lastname}"
            top_3_playersl.append({
                'Player': player_name,
                'Points': str(points),
                'Picture': player_picture
                
            })
    return(top_3_playersl)
    
def top_3_teams():
    url = 'https://api-web.nhle.com/v1/standings/now'
    r= requests.get(url).json()
    top_3 = []
    if 'standings' in r:
        for team in r['standings'][:3]:
            team_name = team.get('teamName', {}).get('default')
            points = team.get('points', {})
            wins = team.get('wins', {})
            losses = team.get('losses', {})
            logo = team.get('teamLogo', {})
            wins_and_losses = f"{wins} - {losses}"
            top_3.append({
                'Team': team_name,
                'wins_losses': wins_and_losses,
                'Points': points,
                'logo': logo
                
            })
    return(top_3)

