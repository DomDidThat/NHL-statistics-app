import json
import requests
import requests_cache
import os
import unittest
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

requests_cache.install_cache('nhl_api_cache', expire_after=3600)

async def fetch_team_rosters(session, abbreviation):
    url = f"https://api-web.nhle.com/v1/roster/{abbreviation}/current"
    async with session.get(url) as response:
        if response.status == 200:
            roster_data = await response.json()
            return [player.get("id") for player in roster_data.get('forwards', [])]
        else:
            return []

async def fetch_player_stats(session, player_id):
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    async with session.get(url) as r:
        if r.status == 200:
            player_data = await r.json()
            return extract_player_stats(player_data)
        else:
            return {"Name": "No player found", "Stats": {}}

def extract_player_stats(player_data):
    player_fname = player_data.get('firstName').get('default')
    player_lname = player_data.get('lastName').get('default')
    team = player_data.get('currentTeamAbbrev')
    featured_stats = player_data.get('featuredStats', {})
    regular_season_stats = featured_stats.get('regularSeason', {})
    player_stats = regular_season_stats.get('subSeason', {})
    return {
        "Name": f"{player_fname} {player_lname}",
        "Team": team,
        "Games Played": player_stats.get('gamesPlayed', 0),
        "Goals": player_stats.get('goals', 0),
        "Assists": player_stats.get('assists', 0),
        "Points": player_stats.get('points', 0),
        "Plus Minus": player_stats.get('plusMinus', 0),
        "Pim": player_stats.get('pim', 0),
        "Game Winning Goals": player_stats.get('gameWinningGoals', 0),
        "OT Goals": player_stats.get('otGoals' , 0),
        "Shots": player_stats.get('shots', 0),
        "Shooting Percentage": format_shooting_percentage(player_stats.get('shootingPctg'))
    }

def format_shooting_percentage(shooting_pctg):
    if shooting_pctg is None:
        return 0
    return "{:.2f}%".format(shooting_pctg * 100)

async def get_all_team_rosters_and_player_stats():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_team_rosters(session, abbreviation) for abbreviation in nhl_team_abbreviations]
        player_ids_lists = await asyncio.gather(*tasks)

        tasks = [fetch_player_stats(session, player_id) for player_ids in player_ids_lists for player_id in player_ids]
        all_player_stats = await asyncio.gather(*tasks)

    return all_player_stats

# Call the function
player_stats = asyncio.run(get_all_team_rosters_and_player_stats())