
import requests
import requests_cache
from datetime import date
import aiohttp
import asyncio
import sys

print(sys.path)

today = date.today()
requests_cache.install_cache('nhl_api_cache', expire_after=3600)

def games():
    """
    Fetches and processes the list of NHL games for the current day from the NHL API.

    This function constructs a request to the NHL API to retrieve the games scheduled for today.
    It then parses the JSON response to extract relevant details about each game, including the
    date, teams involved, their scores, and the game state. These details are compiled into a list
    of dictionaries, where each dictionary represents a single game.

    Returns:
        games_list (list of dict): A list of dictionaries, each containing details about a game.
            The keys in each dictionary include 'game_date', 'home_team_name', 'Game state', and 'Score'.
            'game_date' is a string representing the date of the game.
            'home_team_name' is a string formatted as "HomeTeam vs AwayTeam".
            'Game state' indicates the current state of the game (e.g., "In Progress", "Final").
            'Score' is a string representing the current score of the game, formatted as "HomeScore - AwayScore".

    Note:
        This function assumes that the NHL API's response structure remains consistent and that the 'games'
        key is always present when there are games scheduled for the day. It does not handle API errors or
        unexpected response structures gracefully.
    """
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
    """
    Fetches and returns the top 3 NHL players based on points for the current season.

    This function makes a GET request to the NHL API to retrieve the top 3 players in terms of points.
    It parses the JSON response to extract each player's first name, last name, total points, and picture URL.
    These details are compiled into a list of dictionaries, where each dictionary represents a single player.

    Returns:
        top_3_playersl (list of dict): A list of dictionaries, each containing details about a player.
            The keys in each dictionary include 'Player', 'Points', and 'Picture'.
            'Player' is a string representing the player's full name.
            'Points' is a string representing the total points scored by the player.
            'Picture' is a URL to the player's headshot image.

    Note:
        This function assumes that the NHL API's response structure for the endpoint used remains consistent.
        It does not handle API errors or unexpected response structures gracefully.
    """
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



async def fetch_team_rosters(session, abbreviation):
    """
    Asynchronously fetches the roster for a given NHL team using its abbreviation.

    This function makes an asynchronous GET request to the NHL API to retrieve the current roster
    of a specified team. It extracts and returns the player IDs for all forwards on the team.

    Parameters:
        session (aiohttp.ClientSession): The session used to make the HTTP request.
        abbreviation (str): The abbreviation of the NHL team for which the roster is requested.

    Returns:
        list: A list of player IDs for the forwards on the team's current roster. Returns an empty
        list if the request fails or if the team has no forwards listed in the response.

    Note:
        This function specifically targets the 'forwards' section of the roster in the API response.
        It does not return information about defensemen or goaltenders.
    """
    url = f"https://api-web.nhle.com/v1/roster/{abbreviation}/current"
    async with session.get(url) as response:
        if response.status == 200:
            roster_data = await response.json()
            return [player.get("id") for player in roster_data.get('forwards', [])]
        else:
            return []

async def fetch_player_stats(session, player_id):
    """
    Asynchronously fetches and processes the statistics for a specific NHL player by their ID.

    This function makes an asynchronous GET request to the NHL API to retrieve detailed statistics
    for a player specified by their unique player ID. It then extracts and formats these statistics
    using the `extract_player_stats` function.

    Parameters:
        session (aiohttp.ClientSession): The session used to make the HTTP request.
        player_id (str): The unique identifier for the player whose statistics are being requested.

    Returns:
        dict: A dictionary containing the formatted player statistics if the request is successful.
              If the request fails or the player is not found, it returns a dictionary with the
              player's name set to "No player found" and an empty "Stats" dictionary.

    Note:
        The function returns immediately with a default response if the HTTP status code of the
        response is not 200, indicating a successful request.
    """
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    async with session.get(url) as r:
        if r.status == 200:
            player_data = await r.json()
            return extract_player_stats(player_data)
        else:
            return {"Name": "No player found", "Stats": {}}

def extract_player_stats(player_data):
    """
    Extracts and formats player statistics from the provided player data.

    This function parses the player data dictionary to extract the player's first and last name,
    team abbreviation, and various statistics for the regular season. These statistics include
    games played, goals, assists, total points, plus-minus rating, penalty minutes (PIM),
    game-winning goals, overtime goals, total shots, and shooting percentage. The shooting
    percentage is formatted to a string with two decimal places.

    Parameters:
        player_data (dict): A dictionary containing detailed information about a player,
                            including their name, team, and statistics.

    Returns:
        dict: A dictionary containing the player's name, team, and formatted statistics.
              The keys include "Name", "Team", "Games Played", "Goals", "Assists", "Points",
              "Plus Minus", "Pim", "Game Winning Goals", "OT Goals", "Shots", and
              "Shooting Percentage".

    Note:
        - The function assumes that the input dictionary contains all the necessary keys.
        - If certain statistics are not available, they are defaulted to 0.
        - The shooting percentage is calculated as a percentage and formatted as a string.
    """
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
    """
    Formats a shooting percentage value for display.

    This function takes a shooting percentage as a decimal (e.g., 0.123 for 12.3%) and formats it
    as a string with two decimal places, followed by a percent sign. If the input is None, indicating
    that the shooting percentage is not available, the function returns '0.00%' as a default.

    Parameters:
        shooting_pctg (float or None): The shooting percentage as a decimal. If None, indicates that
                                       the shooting percentage is not available.

    Returns:
        str: The formatted shooting percentage as a string with two decimal places, followed by a percent
             sign. Returns '0.00%' if the input is None.
    """
    if shooting_pctg is None:
        return "0.00%"
    return "{:.2f}%".format(shooting_pctg * 100)

async def get_all_team_rosters_and_player_stats():
    """
    This function uses asynchronous programming to fetch the rosters and player statistics for all NHL teams.

    Parameters:
        session (aiohttp.ClientSession): The aiohttp session object used to make HTTP requests.

    Returns:
        list: A list of dictionaries, where each dictionary represents a player and their statistics for a specific NHL team. The keys include "Name", "Team", "Games Played", "Goals", "Assists", "Points", "Plus Minus", "Pim", "Game Winning Goals", "OT Goals", "Shots", and "Shooting Percentage".

    Note:
        This function uses the aiohttp library for asynchronous HTTP requests.
    """
    async with aiohttp.ClientSession() as session:
        # Get the player IDs for all forwards on each team
        tasks = [fetch_team_rosters(session, abbreviation) for abbreviation in nhl_team_abbreviations]
        player_ids_lists = await asyncio.gather(*tasks)

        # Get the player statistics for each player ID
        tasks = [fetch_player_stats(session, player_id) for player_ids in player_ids_lists for player_id in player_ids]
        all_player_stats = await asyncio.gather(*tasks)

    return all_player_stats

# Call the function
player_stats = asyncio.run(get_all_team_rosters_and_player_stats())