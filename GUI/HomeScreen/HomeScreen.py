import sys
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget


class HomeScreen(QWidget):
    def __init__(self):
        """
        Initializes the HomeScreen widget.

        Sets the window title, geometry, and initializes the user interface.
        """
        super().__init__()

        self.setWindowTitle("NHL Statistics App")
        self.setGeometry(100, 100, 1440, 900)

        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface of the HomeScreen widget.

        Creates the layout and adds the title label, description label, and get started button.
        Sets the fixed size of the container and applies the stylesheet.
        """
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        
        l1_container = QWidget(self)
        l1_container.setObjectName("l1Container")
        l1_container_layout = QVBoxLayout(l1_container)
        
        
        self.title_label = QLabel("Welcome to the NHL Statistics App", self)
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.title_label.setFixedHeight(45)
         
        self.l1 = QLabel("Track player and team stats")
        self.l1.setObjectName("l1")
        self.l1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.l1.setFixedHeight(20)
        
        self.get_started_button = QPushButton("Get Started", self)
        self.get_started_button.setObjectName("getStartedButton")   
        self.get_started_button.setFixedSize(100, 35)
        l2_container = QWidget(self)
        l2_container.setObjectName("l2Container")
        l2_container_layout = QVBoxLayout(l2_container)

        self.tts_label = QLabel("Top Teams")
        self.tts_label.setObjectName("ttsLabel")
        self.tts_label.setAlignment(Qt.AlignLeft)
        self.tts_label.setFixedHeight(50)
        
        self.top_teams_button = QPushButton("Top Teams", self)
        self.top_teams_button.setObjectName("topTeamsButton")
        self.top_teams_button.setFixedSize(100, 35)
        
        l3_container = QWidget(self)    
        l3_container.setObjectName("l3Container")
        l3_container_layout = QVBoxLayout(l3_container)
        
        self.featured_players_label = QLabel("Featured Players")
        self.featured_players_label.setObjectName("featuredPlayersLabel")
        self.featured_players_label.setAlignment(Qt.AlignLeft )
        self.featured_players_label.setFixedHeight(50)
        
        self.view_all_players_button = QPushButton("View All Players", self)
        self.view_all_players_button.setObjectName("viewAllPlayersButton")
        self.view_all_players_button.setFixedSize(100, 35)
        
        l4_container = QWidget(self)
        l4_container.setObjectName("l4Container")
        l4_container_layout = QVBoxLayout(l4_container)
        
        self.player_search_label = QLabel("Search for Players")
        self.player_search_label.setObjectName("playerSearchLabel")
        self.player_search_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.player_search_label.setFixedHeight(50)
        
        self.search_players_sb = QLineEdit(self)
        self.search_players_sb.setPlaceholderText("Enter Player Name")
        self.search_players_sb.setObjectName("searchPlayersSB")
        self.search_players_sb.setFixedSize(300, 25)
        
        self.search_button = QPushButton("Search", self)
        self.search_button.setObjectName("searchButton")
        self.search_button.setFixedSize(100, 35)
        
        l5_container = QWidget(self)
        l5_container.setObjectName("l5Container")
        l5_container_layout = QVBoxLayout(l5_container)
        
        v1_container = QWidget(l5_container)
        v1_container.setObjectName("v1Container")
        v1_container_layout = QVBoxLayout(v1_container)
        
        
        self.about_label = QLabel("About the NHL Statistics App")
        self.about_label.setObjectName("aboutLabel")
        
        l1_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        l2_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        l3_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        l4_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        l5_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        v1_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        l1_container.setFixedSize(1440, 125)
        l2_container.setFixedSize(1440, 200)
        l3_container.setFixedSize(1440, 200)
        l4_container.setFixedSize(1440, 150)
        l5_container.setFixedSize(1440, 200)
        v1_container.setFixedSize(500, 175)
        
        l1_container_layout.addWidget(self.title_label)
        l1_container_layout.addWidget(self.l1)
        l1_container_layout.addWidget(self.get_started_button, alignment=Qt.AlignCenter | Qt.AlignTop)
        
        l2_container_layout.addWidget(self.tts_label)
        l2_container_layout.addWidget(self.top_teams_button, alignment=Qt.AlignLeft )
        
        l3_container_layout.addWidget(self.featured_players_label)
        l3_container_layout.addWidget(self.view_all_players_button, alignment=Qt.AlignLeft)
        
        l4_container_layout.addWidget(self.player_search_label)
        l4_container_layout.addWidget(self.search_players_sb, alignment=Qt.AlignHCenter)
        l4_container_layout.addWidget(self.search_button, alignment=Qt.AlignHCenter)
        
        l5_container_layout.addWidget(v1_container, alignment=Qt.AlignHCenter | Qt.AlignTop)
        l5_container_layout.setAlignment(Qt.AlignHCenter)
        
        v1_container_layout.addWidget(self.about_label)
        v1_container_layout.setAlignment(Qt.AlignHCenter)
        
        
        layout.addWidget(l1_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(l2_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(l3_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(l4_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(l5_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        
        
        
        with open("GUI/HomeScreen/HSStyle.qss", "r") as file:
            stylesheet = file.read()
            
            
        self.setLayout(layout)
        self.setStyleSheet(stylesheet)
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec_())
