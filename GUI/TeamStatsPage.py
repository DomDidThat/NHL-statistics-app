import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt
import asyncio
import requests_cache
from team_stats import team_standings  # Import the function to fetch team data

requests_cache.install_cache("nhl_api_cache", expire_after=3600)

class NumericTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        super().__init__(str(value) if value is not None else "")
        self.value = value

    def __lt__(self, other):
        try:
            return float(self.value or 0) < float(other.value or 0)
        except ValueError:
            return super().__lt__(other)
    
class TeamInformationPage(QWidget):
    def __init__(self, team_data):
        super().__init__()
        self.team_data = team_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.populate_table()
        
        self.sort_button = QPushButton("Sort by Wins")  # Example sort button
        self.sort_button.clicked.connect(self.sort_by_wins)
        layout.addWidget(self.sort_button)
        
        self.sort_losses_button = QPushButton("Sort by Losses")
        self.sort_losses_button.clicked.connect(self.sort_by_losses)
        layout.addWidget(self.sort_losses_button)

    def populate_table(self):
        # Set table dimensions
        num_rows = len(self.team_data)
        num_columns = len(self.team_data[0])

        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_columns)

        # Set table headers
        headers = list(self.team_data[0].keys())
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Populate table with team data
        for row, team in enumerate(self.team_data):
            for col, (key, value) in enumerate(team.items()):
                if col in [3, 4]:  # Assuming 'Wins' and 'Losses' columns are at index 3 and 4 respectively
                    item = NumericTableWidgetItem(value)
                else:
                    item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)      
                
                
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size to prevent it from becoming too small
                
    def sort_by_wins(self):
        self.table_widget.sortItems(2, Qt.DescendingOrder)
        
    def sort_by_losses(self):
        self.table_widget.sortItems(3, Qt.DescendingOrder)  # Sorts by the 'Losses' column (index 4) in descending order

async def fetch_team_data():
    # Fetch team data asynchronously
    team_data = await team_standings()  # Use the appropriate function to fetch team data
    return team_data

    
def main():
    app = QApplication(sys.argv)

    # Fetch team data asynchronously
    team_data = asyncio.run(fetch_team_data())

    # Create and display the TeamInformationPage
    team_info_page = TeamInformationPage(team_data)
    team_info_page.setWindowTitle("Team Information")
    team_info_page.resize(600, 400)
    team_info_page.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
