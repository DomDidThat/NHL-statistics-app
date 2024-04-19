import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHeaderView, QMessageBox, QSizePolicy
from PyQt5.QtCore import Qt
import requests_cache
from shared import get_all_team_rosters_and_player_stats

# Install the cache with a specified expiration time (in seconds)
requests_cache.install_cache("nhl_api_cache", expire_after=3600)

class PlayerStatsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Player Stats")
        
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.sort_goals_button = QPushButton("Sort by Goals")
        layout.addWidget(self.sort_goals_button)
        self.sort_goals_button.clicked.connect(self.sort_by_goals)

        self.sort_assists_button = QPushButton("Sort by Assists")
        layout.addWidget(self.sort_assists_button)
        self.sort_assists_button.clicked.connect(self.sort_by_assists)

        self.sort_points_button = QPushButton("Sort by Points")
        layout.addWidget(self.sort_points_button)
        self.sort_points_button.clicked.connect(self.sort_by_points)
        
        asyncio.run(self.fetch_and_display_player_data())
        
    async def fetch_player_data(self):
        # Fetch player data asynchronously
        try:
            player_data = await get_all_team_rosters_and_player_stats()
            return player_data
        except Exception as e:
            # If an error occurs during fetching, return None and handle the error in fetch_and_display_player_data
            return None

    async def fetch_and_display_player_data(self):
        player_data = await self.fetch_player_data()
        if player_data is not None:
            # Populate table with player data
            self.populate_table(player_data)
        else:
            QMessageBox.critical(self, "Error", "Failed to fetch player data.")

    def populate_table(self, player_data):
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
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)
                if col in [3, 4, 5]:
                    item = QTableWidgetItem()
                    item.setData(Qt.DisplayRole, float(value))
                else: 
                    item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size to prevent it from becoming too small

    def sort_by_goals(self):
            self.table_widget.sortItems(3, Qt.DescendingOrder)  # Assuming 'Goals' column is at index 3
        

    def sort_by_assists(self):
        self.table_widget.sortItems(4, Qt.DescendingOrder)  # Assuming 'Assists' column is at index 4

    def sort_by_points(self):
        self.table_widget.sortItems(5, Qt.DescendingOrder)  # Assuming 'Points' column is at index 5
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = PlayerStatsDialog()
    try:
        dialog.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
