import json
import requests
import requests_cache
import os
import unittest
from datetime import date
import aiohttp
import asyncio
from shared import format_shooting_percentage

def top_3_teams():
    """
    Fetches and returns the top 3 teams from the NHL standings.

    This function makes a GET request to the NHL standings API, extracts the top 3 teams,
    and formats their information into a list of dictionaries. Each dictionary contains
    the team's name, wins and losses record, points, and logo URL.

    Returns:
        list of dict: A list containing dictionaries for each of the top 3 teams. Each dictionary
        includes the team's name ('Team'), wins and losses record ('wins_losses'), points ('Points'),
        and logo URL ('logo'). If the 'standings' key is not present in the response, an empty list is returned.
    """
    url = 'https://api-web.nhle.com/v1/standings/now'
    r = requests.get(url).json()  # Sends a GET request to the NHL standings API.
    top_3 = []  # Initializes an empty list to store the top 3 teams' information.
    if 'standings' in r:  # Checks if the 'standings' key is present in the API response.
        for team in r['standings'][:3]:  # Iterates over the top 3 teams in the standings.
            team_name = team.get('teamName', {}).get('default')  # Extracts the team's name.
            points = team.get('points', {})  # Extracts the team's points.
            wins = team.get('wins', {})  # Extracts the number of wins.
            losses = team.get('losses', {})  # Extracts the number of losses.
            logo = team.get('teamLogo', {})  # Extracts the team's logo URL.
            wins_and_losses = f"{wins} - {losses}"  # Formats the wins and losses record.
            top_3.append({
                'Team': team_name,
                'wins_losses': wins_and_losses,
                'Points': points,
                'logo': logo
                
            })  # Appends the team's information as a dictionary to the top_3 list.
    
    return top_3  # Returns the list of top 3 teams.

async def team_standings():
    url = 'https://api-web.nhle.com/v1/standings/now'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
    team_standings = []
    if 'standings' in r:
        for team in r['standings']:
            team_name = team.get('teamName', {}).get('default')
            points = team.get('points', {})
            wins = team.get('wins', {})
            losses = team.get('losses', {})
            games_played = team.get('gamesPlayed', 0)
            goal_differential = team.get('goalDifferential', 0)
            goal_differential_percentage = team.get('goalDifferentialPctg', 0)
            goal_against = team.get('goalAgainst', 0)
            goal_for = team.get('goalFor', 0)
            goals_for_percentage = team.get('goalsForPctg', 0)
            
            team_standings.append({
                'Team': team_name,
                'Games Played': games_played,
                'Wins': wins,
                'Losses': losses,
                'Points': points,
                'Goal Differential': goal_differential,
                'Goal Differential Percentage': format_shooting_percentage(goal_differential_percentage),
                'Goal Against': goal_against,
                'Goal For': goal_for,
                'Goals For Percentage': format_shooting_percentage(goals_for_percentage),
            })
    return team_standings
async def main():
    standings = await team_standings()
    return standings

if __name__ == '__main__':
    asyncio.run(main())

