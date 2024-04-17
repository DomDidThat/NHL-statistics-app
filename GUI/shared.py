import json
import requests
import requests_cache
import os
from datetime import date
import aiohttp
import asyncio

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


nhl_team_abbreviations = [
    "ANA",  # Anaheim Ducks
    "ARI",  # Arizona Coyotes
    "BOS",  # Boston Bruins
    "BUF",  # Buffalo Sabres
    "CGY",  # Calgary Flames
    "CAR",  # Carolina Hurricanes
    "CHI",  # Chicago Blackhawks
    "COL",  # Colorado Avalanche
    "CBJ",  # Columbus Blue Jackets
    "DAL",  # Dallas Stars
    "DET",  # Detroit Red Wings
    "EDM",  # Edmonton Oilers
    "FLA",  # Florida Panthers
    "LAK",  # Los Angeles Kings
    "MIN",  # Minnesota Wild
    "MTL",  # Montreal Canadiens
    "NSH",  # Nashville Predators
    "NJD",  # New Jersey Devils
    "NYI",  # New York Islanders
    "NYR",  # New York Rangers
    "OTT",  # Ottawa Senators
    "PHI",  # Philadelphia Flyers
    "PIT",  # Pittsburgh Penguins
    "SJS",  # San Jose Sharks
    "STL",  # St. Louis Blues
    "TBL",  # Tampa Bay Lightning
    "TOR",  # Toronto Maple Leafs
    "VAN",  # Vancouver Canucks
    "VGK",  # Vegas Golden Knights
    "WSH",  # Washington Capitals
    "WPG",  # Winnipeg Jets
]



async def fetch_team_rosters(session, abbreviation):
    url = f"https://api-web.nhle.com/v1/roster/{abbreviation}/current"
    async with session.get(url) as response:
        if response.status == 200:
            roster_data = await response.json()
            players = roster_data.get('forwards', [])
            return [
                player.get("id")
             for player in players]
        else:
            return []

async def fetch_player_stats(session, player_id):
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    async with session.get(url) as r:
        if r.status == 200:
            player_data = await r.json()
            featured_stats = player_data.get('featuredStats',{})
            regular_season_stats = featured_stats.get('regularSeason', {})
            player_stats = regular_season_stats.get('subSeason', {})
            games_played = player_stats.get('gamesPlayed',{})
            goals = player_stats.get('goals')
            assists = player_stats.get('assists')
            points = player_stats.get('points')
            player_first_name = player_data.get('firstName', {}).get('default')
            player_last_name = player_data.get('lastName', {}).get('default')
            return {
                "Name": f"{player_first_name} {player_last_name}",
                "Games Played" : games_played,
                "Goals" : goals,
                "Assists": assists,
                "Points" : points
                
            }
        else:
            return {"Name": "No player found", "Stats": {}}

async def get_all_team_rosters_and_player_stats():
    all_player_stats = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for abbreviation in nhl_team_abbreviations:
            player_ids = await fetch_team_rosters(session, abbreviation)
            tasks.extend([fetch_player_stats(session, player_id) for player_id in player_ids])
        player_stats = await asyncio.gather(*tasks)
        all_player_stats.extend(player_stats)
    return all_player_stats


# Call the function
player_stats = asyncio.run(get_all_team_rosters_and_player_stats())


