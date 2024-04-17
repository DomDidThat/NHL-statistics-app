import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import asyncio
from shared import get_all_team_rosters_and_player_stats

class PlayerInformationPage(QWidget):
    def __init__(self, player_data):
        super().__init__()
        self.player_data = player_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.populate_table()

    def populate_table(self):
        # Set table dimensions
        num_rows = len(self.player_data)
        num_columns = len(self.player_data[0])

        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_columns)

        # Set table headers
        headers = list(self.player_data[0].keys())
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Populate table with player data
        for row, player in enumerate(self.player_data):
            for col, (key, value) in enumerate(player.items()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

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
