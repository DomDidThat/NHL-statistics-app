from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QMessageBox, QSizePolicy, QApplication
from PyQt5.QtCore import Qt
import asyncio
import sys

from team_stats import team_standings  # Import the function to fetch team data

class TeamStatsDialog(QDialog):
    def __init__(self, parent=None):
        """
        Initializes the TeamStatsDialog window with a table widget and a sort button.

        This method sets up the UI components for the TeamStatsDialog, including a table to display team statistics
        and a button to sort these statistics by wins. It also triggers the asynchronous fetching and displaying of
        team data upon initialization.

        Parameters:
        - parent: The parent widget of this dialog. Defaults to None.

        The layout is a QVBoxLayout, which arranges the table widget and the sort button vertically.
        The sort button is connected to the sort_by_wins method, which sorts the table's contents.
        The fetch_and_display_team_data coroutine is called to asynchronously fetch and display the team data.
        """
        super().__init__(parent)
        self.setWindowTitle("Team Stats")
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.sort_button = QPushButton("Sort by Wins")
        layout.addWidget(self.sort_button)
        self.sort_button.clicked.connect(self.sort_by_wins)

        # Fetch and display team data
        asyncio.run(self.fetch_and_display_team_data())

    async def fetch_and_display_team_data(self):
        """
        Asynchronously fetches team data and populates the table widget with this data.

        This method attempts to fetch team data using the `fetch_team_data` coroutine. Upon successful
        retrieval of the data, it calls `populate_table` to display the data in the table widget. If an
        error occurs during the fetch operation, it displays an error message dialog.

        Exceptions:
            Exception: Catches and handles any exception that occurs during the fetch operation, displaying
                    an error message dialog to the user.
        """
        try:
            # Fetch team data asynchronously
            team_data = await fetch_team_data()

            # Populate table with team data
            self.populate_table(team_data)
        except Exception as e:
            # Handle exceptions by displaying an error message to the user
            QMessageBox.critical(self, "Error", f"Failed to fetch team data: {str(e)}")

    def populate_table(self, team_data):
        """
        Populates the table widget with team data.

        This method sets the table dimensions based on the number of items in the team_data list and the number of keys in the first item of the list, which represent the columns. It then sets the table headers using the keys from the first item in the team_data list. Each item in the team_data list is a dictionary representing a team, with keys as column headers and values as the data for those columns. The method iterates over each team in the team_data list, creating a QTableWidgetItem for each piece of data and adding it to the table widget.

        Parameters:
        - team_data (list of dict): A list of dictionaries, where each dictionary contains data about a team.

        Returns:
        - None
        """
        # Set table dimensions
        num_rows = len(team_data)
        num_columns = len(team_data[0])

        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_columns)

        # Set table headers
        headers = list(team_data[0].keys())
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Populate table with team data
        for row, team in enumerate(team_data):
            for col, (key, value) in enumerate(team.items()):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size to prevent it from becoming too small  # Set a minimum size to prevent it from becoming too small

    def sort_by_wins(self):
        """
        Sorts the table rows based on the 'Wins' column in descending order.

        This method sorts the entries in the table widget according to the number of wins, with the team having the highest number of wins appearing first. It assumes that the 'Wins' column is at index 2 of the table.

        Parameters:
        - None

        Returns:
        - None
        """
        self.table_widget.sortItems(2, Qt.DescendingOrder)  # Assuming 'Wins' column is at index 2  # Assuming 'Wins' column is at index 2
            
async def fetch_team_data():
    """
    Asynchronously fetches and returns team data using the team_standings function.

    This function is an asynchronous wrapper around the `team_standings` function, which is assumed to fetch
    team data from an external source asynchronously. It awaits the completion of `team_standings` and returns
    the fetched data.

    Returns:
        list of dict: A list of dictionaries, where each dictionary contains data about a team. The exact structure
        of these dictionaries depends on the implementation of `team_standings`.
    """
    team_data = await team_standings()  # Use the appropriate function to fetch team data
    return team_data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TeamStatsDialog()
    try:
        dialog.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
