import unittest
from shared import fetch_team_rosters, extract_player_stats, get_all_team_rosters_and_player_stats
import asyncio
import aiohttp
from unittest.mock import MagicMock, patch
import sys
print(sys.path)


class TestFetchTeamRosters(unittest.TestCase):
    @patch('shared.aiohttp.ClientSession.get')
    async def test_fetch_team_rosters(self, mock_get):
        # Mocking the response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json.return_value = {'forwards': [{'id': '123'}, {'id': '456'}]}
        
        # Patching the get method to return the mock response
        mock_get.return_value.__aenter__.return_value = mock_response

        # Creating a mock session
        session = aiohttp.ClientSession()

        # Calling the asynchronous function
        roster_ids = await fetch_team_rosters(session, 'NJD')

        # Asserting the result
        mock_roster_ids = ['123', '456']
        self.assertEqual(roster_ids, mock_roster_ids)
        
class TestExtractPlayerStats(unittest.TestCase):
    
    def test_extract_player_stats(self):
        """
        Test the `extract_player_stats` function to ensure it correctly transforms player data into a specified format.

        This test provides a mock player data dictionary, simulating the structure that would be received from an external
        API. It then calls the `extract_player_stats` function with this mock data and compares the result to an expected
        dictionary format, asserting equality to verify correct functionality.

        The expected result includes formatted player statistics such as name, team, and various performance metrics,
        demonstrating the function's ability to parse and reformat nested data structures.
        """
        player_data = {
            'firstName': {'default': 'John'},
            'lastName': {'default': 'Doe'},
            'currentTeamAbbrev': 'NYR',
            'featuredStats': {
                'regularSeason': {
                    'subSeason': {
                        'gamesPlayed': 82,
                        'goals': 20,
                        'assists': 30,
                        'points': 50,
                        'plusMinus': 10,
                        'pim': 40,
                        'gameWinningGoals': 5,
                        'otGoals': 2,
                        'shots': 150,
                        'shootingPctg': 0.13333
                    }
                }
            }
        }

        expected_result = {
            "Name": "John Doe",
            "Team": "NYR",
            "Games Played": 82,
            "Goals": 20,
            "Assists": 30,
            "Points": 50,
            "Plus Minus": 10,
            "Pim": 40,
            "Game Winning Goals": 5,
            "OT Goals": 2,
            "Shots": 150,
            "Shooting Percentage": "13.33%"
        }

        result = extract_player_stats(player_data)
        self.assertEqual(result, expected_result)
        
class TestGetAllTeamRostersAndPlayerStats(unittest.TestCase):
    @patch('shared.fetch_team_rosters')
    @patch('shared.fetch_player_stats')
    @patch('shared.aiohttp.ClientSession')
    async def test_get_all_team_rosters_and_player_stats(self, mock_session, mock_fetch_player_stats, mock_fetch_team_rosters):
        # Mocking the aiohttp session
        mock_session.return_value.__aenter__.return_value = MagicMock()

        # Mocking fetch_team_rosters to return a list of player IDs for each team
        mock_fetch_team_rosters.side_effect = lambda session, abbreviation: asyncio.Future().set_result(['player1', 'player2'])

        # Mocking fetch_player_stats to return a dictionary of player stats
        mock_fetch_player_stats.side_effect = lambda session, player_id: asyncio.Future().set_result({'Name': 'Player Name', 'Team': 'Team Name', 'Goals': 10})

        # Running the asynchronous function
        all_player_stats = await get_all_team_rosters_and_player_stats()

        # Assertions to ensure the function behaves as expected
        self.assertIsInstance(all_player_stats, list)
        self.assertGreater(len(all_player_stats), 0)
        self.assertIn('Name', all_player_stats[0])
        self.assertIn('Team', all_player_stats[0])
        self.assertIn('Goals', all_player_stats[0])

        # Ensure the mock functions were called as expected
        mock_fetch_team_rosters.assert_called()
        mock_fetch_player_stats.assert_called()

        
if __name__ == '__main__':
    unittest.main()
    asyncio.run(unittest.main(), debug=True)