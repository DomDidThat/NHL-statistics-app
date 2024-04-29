import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHeaderView, QMessageBox, QSizePolicy
from PyQt5.QtCore import Qt
from shared import get_all_team_rosters_and_player_stats

class PlayerStatsDialog(QDialog):
    def __init__(self, parent=None):
        """
        Initialize the PlayerStatsDialog window with a table and sorting buttons.

        This method sets up the UI for the PlayerStatsDialog, including a table to display player stats
        and buttons to sort these stats by goals, assists, and points. It also initiates the asynchronous
        fetching and displaying of player data.

        Parameters:
        - parent: The parent widget of this dialog. Defaults to None.

        Returns:
        None
        """
        super().__init__(parent)
        self.setWindowTitle("Player Stats")
        
        # Set up the layout for the dialog
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and add the table widget to the layout
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Create and add the "Sort by Goals" button to the layout
        self.sort_goals_button = QPushButton("Sort by Goals")
        layout.addWidget(self.sort_goals_button)
        self.sort_goals_button.clicked.connect(self.sort_by_goals)

        # Create and add the "Sort by Assists" button to the layout
        self.sort_assists_button = QPushButton("Sort by Assists")
        layout.addWidget(self.sort_assists_button)
        self.sort_assists_button.clicked.connect(self.sort_by_assists)

        # Create and add the "Sort by Points" button to the layout
        self.sort_points_button = QPushButton("Sort by Points")
        layout.addWidget(self.sort_points_button)
        self.sort_points_button.clicked.connect(self.sort_by_points)
        
        # Asynchronously fetch and display player data
        asyncio.run(self.fetch_and_display_player_data())
        
    async def fetch_player_data(self):
        """
        Asynchronously fetches player data using the get_all_team_rosters_and_player_stats function.

        This method attempts to retrieve player data asynchronously. If successful, it returns the fetched data.
        In case of any exception, it returns None and expects the calling method to handle the error appropriately.

        Returns:
            player_data (dict or None): The fetched player data as a dictionary if the fetch is successful, or None if an exception occurs.
        """
        try:
            player_data = await get_all_team_rosters_and_player_stats()
            return player_data
        except Exception as e:
            # If an error occurs during fetching, return None and handle the error in fetch_and_display_player_data
            return None

    async def fetch_and_display_player_data(self):
        """
        Asynchronously fetches player data and displays it in the table widget.

        This method first attempts to fetch player data asynchronously. If the data is successfully retrieved,
        it calls the populate_table method to display the data in the table widget. If the fetch operation fails,
        it displays an error message to the user using a QMessageBox.

        Parameters:
        None

        Returns:
        None
        """
        player_data = await self.fetch_player_data()
        if player_data is not None:
            # Populate table with player data
            self.populate_table(player_data)
        else:
            QMessageBox.critical(self, "Error", "Failed to fetch player data.")

    def populate_table(self, player_data):
        """
        Populates the table widget with player data.

        This method sets the table dimensions based on the number of players (rows) and the number of attributes
        per player (columns). It then sets the table headers using the keys from the first player's dictionary.
        Each player's data is inserted into the table, with special handling for numeric values in columns 3, 4, and 5
        to ensure they are displayed correctly. Finally, it adjusts the table's appearance and sets a minimum size
        for the dialog.

        Parameters:
        - player_data (list of dict): A list where each element is a dictionary representing a player's statistics.

        Returns:
        None
        """
        # Set table dimensions
        num_rows = len(player_data)
        num_columns = len(player_data[0])

        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_columns)

        # Set table headers
        headers = list(player_data[0].keys())
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Populate table with player data
        for row, player in enumerate(player_data):
            for col, (key, value) in enumerate(player.items()):
                if col in [3, 4, 5]:  # Special handling for numeric values in specific columns
                    item = QTableWidgetItem()
                    item.setData(Qt.DisplayRole, float(value))
                else: 
                    item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size for the dialog  # Set a minimum size to prevent it from becoming too small

    def sort_by_goals(self):
        """
        Sorts the table rows based on the 'Goals' column in descending order.

        This method sorts the player data displayed in the table widget, arranging the players by their goal count
        from highest to lowest. It assumes that the 'Goals' data is located in the fourth column (index 3) of the table.

        Parameters:
        None

        Returns:
        None
        """
        self.table_widget.sortItems(3, Qt.DescendingOrder)  # Assuming 'Goals' column is at index 3  # Assuming 'Goals' column is at index 3
        

    def sort_by_assists(self):
        """
        Sorts the table rows based on the 'Assists' column in descending order.

        This method sorts the player data displayed in the table widget, arranging the players by their assist count
        from highest to lowest. It assumes that the 'Assists' data is located in the fifth column (index 4) of the table.

        Parameters:
        None

        Returns:
        None
        """
        self.table_widget.sortItems(4, Qt.DescendingOrder)  # Assuming 'Assists' column is at index 4  # Assuming 'Assists' column is at index 4

    def sort_by_points(self):
        """
        Sorts the table rows based on the 'Points' column in descending order.

        This method sorts the player data displayed in the table widget, arranging the players by their points count
        from highest to lowest. It assumes that the 'Points' data is located in the sixth column (index 5) of the table.

        Parameters:
        None

        Returns:
        None
        """
        self.table_widget.sortItems(5, Qt.DescendingOrder)  # Assuming 'Points' column is at index 5  # Assuming 'Points' column is at index 5
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = PlayerStatsDialog()
    try:
        dialog.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
