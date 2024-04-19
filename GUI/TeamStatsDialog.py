from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QMessageBox, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
import asyncio
from TeamStatsPage import fetch_team_data

class TeamStatsDialog(QDialog):
    def __init__(self, parent=None):
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
        try:
            # Fetch team data asynchronously
            team_data = await fetch_team_data()

            # Populate table with team data
            self.populate_table(team_data)
        except Exception as e:
            # Handle exceptions
            QMessageBox.critical(self, "Error", f"Failed to fetch team data: {str(e)}")

    def populate_table(self, team_data):
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
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(800, 600)  # Set a minimum size to prevent it from becoming too small

    def sort_by_wins(self):
        self.table_widget.sortItems(2, Qt.DescendingOrder)  # Assuming 'Wins' column is at index 2
