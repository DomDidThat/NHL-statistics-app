import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt
import asyncio
import requests_cache
from shared import get_all_team_rosters_and_player_stats

requests_cache.install_cache("nhl_api_cache", expire_after=3600)

class NumericTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        """
        Initialize a new instance of NumericTableWidgetItem with a given value.

        This constructor overrides the QTableWidgetItem constructor, ensuring that
        the item can handle numeric sorting by storing the original value. If the
        provided value is None, it initializes the item with an empty string. Otherwise,
        it converts the value to a string for display purposes.

        Parameters:
        - value: The numeric value to be stored in the table widget item. Can be of
                 type int, float, or None.

        The value is also stored in a member variable to facilitate comparison operations.
        """
        super().__init__(str(value) if value is not None else "")
        self.value = value

    def __lt__(self, other):
        """
    Override the less-than operator for sorting purposes.

    This method allows instances of NumericTableWidgetItem to be compared
    and sorted based on their numeric value. If the value cannot be converted
    to a float, it falls back to the default QTableWidgetItem comparison.

    Parameters:
    - self: The current instance of NumericTableWidgetItem.
    - other: Another instance of NumericTableWidgetItem to compare against.

    Returns:
    - bool: True if the value of the current instance is less than the value
      of the 'other' instance, False otherwise.
    """
        try:
            return float(self.value or 0) < float(other.value or 0)
        except ValueError:
            return super().__lt__(other)
    
class PlayerInformationPage(QWidget):
    def __init__(self, player_data):
        """
    Initialize the PlayerInformationPage widget with player data.

    This constructor initializes the PlayerInformationPage instance by setting up the UI and storing the player data provided as a parameter. 
    The player data is expected to be a list of dictionaries, where each dictionary represents the data for a single player.

    Parameters:
    - player_data: A list of dictionaries, where each dictionary contains player information such as name, team, goals, assists, and points.

    The initialization process involves setting the player data for the instance and then calling the init_ui method to set up the user interface components.
    """
        super().__init__()
        self.player_data = player_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.populate_table()
        
        self.sort_button = QPushButton("Sort by Goals")  # Example sort button
        self.sort_button.clicked.connect(self.sort_by_goals)
        layout.addWidget(self.sort_button)
        
        self.sort_assists_button = QPushButton("Sort by Assists")
        self.sort_assists_button.clicked.connect(self.sort_by_assists)
        layout.addWidget(self.sort_assists_button)

        self.sort_points_button = QPushButton("Sort by Points")
        self.sort_points_button.clicked.connect(self.sort_by_points)
        layout.addWidget(self.sort_points_button)

    def populate_table(self):
        """
        Populates the table widget with player data.

        This method sets the number of rows and columns based on the player data, sets the table headers, 
        and fills each cell with the appropriate player information. Numeric values for goals, assists, and points are handled by a custom QTableWidgetItem 
        to ensure proper sorting.

        The columns for goals, assists, and points are assumed to be at indices 3, 4, and 5 respectively. 
        This method uses the NumericTableWidgetItem for these columns to enable numeric sorting.
        
        """
        # Set table dimensions
        num_rows = len(self.player_data)  # Determine the number of rows needed from the player data length
        num_columns = len(self.player_data[0])  # Determine the number of columns from the keys of the first player dictionary

        self.table_widget.setRowCount(num_rows)  # Set the number of rows in the table
        self.table_widget.setColumnCount(num_columns)  # Set the number of columns in the table

        # Set table headers
        headers = list(self.player_data[0].keys())  # Extract headers from the keys of the first player dictionary
        self.table_widget.setHorizontalHeaderLabels(headers)  # Set the headers in the table widget

        # Populate table with player data
        for row, player in enumerate(self.player_data):  # Iterate over each player in the player data
            for col, (key, value) in enumerate(player.items()):  # Iterate over each key-value pair in the player dictionary
                if col in [3, 4, 5]:  # Check if the current column is for goals, assists, or points
                    item = NumericTableWidgetItem(value)  # Use NumericTableWidgetItem for numeric sorting
                else:
                    item = QTableWidgetItem(str(value))  # Use standard QTableWidgetItem for other values
                self.table_widget.setItem(row, col, item)  # Set the item in the table widget
                    
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Adjust column width to fit contents
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size to prevent it from becoming too small
                
    def sort_by_goals(self):
        self.table_widget.sortItems(3, Qt.DescendingOrder)
        
    def sort_by_assists(self):
        self.table_widget.sortItems(4, Qt.DescendingOrder)  # Sorts by the 'Assists' column (index 4) in descending order

    def sort_by_points(self):
        self.table_widget.sortItems(5, Qt.DescendingOrder)  # Sorts by the 'Points' column (index 5) in descending order

async def fetch_player_data():
    # Fetch player data asynchronously
    player_data = await get_all_team_rosters_and_player_stats()
    return player_data

    
def main():
    app = QApplication(sys.argv)

    # Fetch player data asynchronously
    player_data = asyncio.run(fetch_player_data())

    # Create and display the PlayerInformationPage
    player_info_page = PlayerInformationPage(player_data)
    player_info_page.setWindowTitle("Player Information")
    player_info_page.resize(600, 400)
    player_info_page.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    