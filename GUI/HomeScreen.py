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
        l2_container_layout = QHBoxLayout(l2_container)
        l2_container_layout.setSpacing(0)
        l2_container.setContentsMargins(0, 0, 0, 0)
        
        v2_container = QWidget(l2_container)
        v2_container.setObjectName("v2Container")
        v2_container_layout = QVBoxLayout(v2_container)
        v2_container_layout.setSpacing(0)
        v2_container.setContentsMargins(0, 0, 0, 0)
        
        s2_container = QWidget(l2_container)
        s2_container.setObjectName("s2Container")
        s2_container_layout = QVBoxLayout(s2_container)
        s2_container_layout.setSpacing(0)
        s2_container.setContentsMargins(0, 0, 0, 0)
        
        tp_container = QWidget(s2_container)
        tp_container.setObjectName("tpContainer")
        tp_container_layout = QVBoxLayout(tp_container)
        
       
        self.tts_label = QLabel("Top Teams")
        self.tts_label.setObjectName("ttsLabel")
        self.tts_label.setAlignment(Qt.AlignLeft)
        self.tts_label.setFixedHeight(50)
        
        self.top_teams_button = QPushButton("Top Teams", self)
        self.top_teams_button.setObjectName("topTeamsButton")
        self.top_teams_button.setFixedSize(100, 35)
        
        tn1 = QLabel("Team Name")
        tn1.setObjectName("tn1")
        tn1.setFixedHeight(15)
        
        td1 = QLabel("Team Data")
        td1.setObjectName("td1")
        td1.setFixedHeight(15)
        
        s3_container = QWidget(l2_container)
        s3_container.setObjectName("s3Container")
        s3_container_layout = QVBoxLayout(s3_container)
        s3_container_layout.setSpacing(0)
        s3_container.setContentsMargins(0, 0, 0, 0)
        
        
        tp2_container = QWidget(s3_container)
        tp2_container.setObjectName("tpContainer")
        tp2_container_layout = QVBoxLayout(tp2_container)
        
        tn2 = QLabel("Team Name")
        tn2.setObjectName("tn2")
        tn2.setFixedHeight(15)
        
        td2 = QLabel("Team Data")
        td2.setObjectName("td2")
        td2.setFixedHeight(15)
        
        s4_container = QWidget(l2_container)
        s4_container.setObjectName("s4Container")
        s4_container_layout = QVBoxLayout(s4_container) 
        s4_container_layout.setSpacing(0)
        s4_container.setContentsMargins(0, 0, 0, 0)
        
        tp3_container = QWidget(s4_container)
        tp3_container.setObjectName("tp3Container")
        tp3_container_layout = QVBoxLayout(tp3_container)
        
        tn3 = QLabel("Team Name")
        tn3.setObjectName("tn3")
        tn3.setFixedHeight(15)
        
        td3 = QLabel("Team Data")
        td3.setObjectName("td3")
        td3.setFixedHeight(15)
        
        l3_container = QWidget(self)    
        l3_container.setObjectName("l3Container")
        l3_container_layout = QHBoxLayout(l3_container)
        
        v3_container = QWidget(l3_container)
        v3_container.setObjectName("v3Container")
        v3_container_layout = QVBoxLayout(v3_container)
        
        self.featured_players_label = QLabel("Featured Players")
        self.featured_players_label.setObjectName("featuredPlayersLabel")
        self.featured_players_label.setAlignment(Qt.AlignLeft )
        self.featured_players_label.setFixedHeight(50)
        
        self.view_all_players_button = QPushButton("View All Players", self)
        self.view_all_players_button.setObjectName("viewAllPlayersButton")
        self.view_all_players_button.setFixedSize(100, 35)
        
        fp1_container = QWidget(l3_container)
        fp1_container.setObjectName("fp1Container")
        fp1_container_layout = QVBoxLayout(fp1_container)
        
        fp1_name = QLabel("Player Name")
        fp1_name.setObjectName("featuredPlayer1")
        fp1_name.setFixedHeight(15)
        
        fp1_data = QLabel("Player Data")
        fp1_data.setObjectName("featuredPlayer1Data")
        fp1_data.setFixedHeight(15)
        
        fp2_container = QWidget(l3_container)
        fp2_container.setObjectName("fp2Container")
        fp2_container_layout = QVBoxLayout(fp2_container)
        
        fp2_name = QLabel("Player Name")
        fp2_name.setObjectName("featuredPlayer2")
        fp2_name.setFixedHeight(15)
        
        fp2_data = QLabel("Player Data")
        fp2_data.setObjectName("featuredPlayer2Data")
        fp2_data.setFixedHeight(15)
        
        fp3_container = QWidget(l3_container)
        fp3_container.setObjectName("fp3Container")
        fp3_container_layout = QVBoxLayout(fp3_container)
        
        fp3_name = QLabel("Player Name")
        fp3_name.setObjectName("featuredPlayer3")
        fp3_name.setFixedHeight(15)
        
        fp3_data = QLabel("Player Data")
        fp3_data.setObjectName("featuredPlayer3Data")
        fp3_data.setFixedHeight(15)
        
        
        
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
        
        s2_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        s3_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        
        l1_container.setFixedSize(1440, 125)
        l2_container.setFixedSize(1440, 200)
        l3_container.setFixedSize(1440, 200)
        l4_container.setFixedSize(1440, 150)
        l5_container.setFixedSize(1440, 200)
        
        v1_container.setFixedSize(500, 175)
        v2_container.setFixedSize(250, 175)
        v3_container.setFixedSize(370, 175)
        
        tp_container.setFixedSize(50, 50)
        tp2_container.setFixedSize(50, 50)
        
        s2_container.setFixedSize(200, 175)
        s3_container.setFixedSize(200, 175)
        s4_container.setFixedSize(200, 175)
        
        fp1_container.setFixedSize(200, 175)
        fp2_container.setFixedSize(200, 175)
        fp3_container.setFixedSize(200, 175)
        
        l1_container_layout.addWidget(self.title_label)
        l1_container_layout.addWidget(self.l1)
        l1_container_layout.addWidget(self.get_started_button, alignment=Qt.AlignCenter | Qt.AlignTop)
        
        l2_container_layout.setAlignment(Qt.AlignLeft)
        l2_container_layout.addWidget(v2_container, alignment=Qt.AlignLeft)
        l2_container_layout.addSpacing(300)
        l2_container_layout.addWidget(s2_container, alignment=Qt.AlignHCenter)
        l2_container_layout.addSpacing(50)
        l2_container_layout.addWidget(s3_container, alignment=Qt.AlignLeft)
        l2_container_layout.addSpacing(50)
        l2_container_layout.addWidget(s4_container, alignment=Qt.AlignLeft)
        
        v2_container_layout.addWidget(self.tts_label)
        v2_container_layout.addWidget(self.top_teams_button, alignment=Qt.AlignLeft )
        v2_container_layout.setAlignment(Qt.AlignLeft)
        
        s2_container_layout.addWidget(tp_container)
        s2_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        s2_container_layout.addWidget(tn1)
        s2_container_layout.addWidget(td1)
        
        s3_container_layout.addWidget(tp2_container)
        s3_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        s3_container_layout.addWidget(tn2)
        s3_container_layout.addWidget(td2)
        
        s4_container_layout.addWidget(tp3_container)
        s4_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        s4_container_layout.addWidget(tn3)
        s4_container_layout.addWidget(td3)
        
        l3_container_layout.setAlignment(Qt.AlignLeft)
        l3_container_layout.addWidget(v3_container, alignment=Qt.AlignLeft)
        l3_container_layout.addSpacing(165)
        l3_container_layout.addWidget(fp1_container, alignment=Qt.AlignHCenter)
        l3_container_layout.addSpacing(50)
        l3_container_layout.addWidget(fp2_container, alignment=Qt.AlignLeft)
        l3_container_layout.addSpacing(50)
        l3_container_layout.addWidget(fp3_container, alignment=Qt.AlignLeft)
        
        fp1_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        fp1_container_layout.addWidget(fp1_name)
        fp1_container_layout.addWidget(fp1_data)
        
        fp2_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        fp2_container_layout.addWidget(fp2_name)
        fp2_container_layout.addWidget(fp2_data)
        
        fp3_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        fp3_container_layout.addWidget(fp3_name)
        fp3_container_layout.addWidget(fp3_data)
        
        
        v3_container_layout.addWidget(self.featured_players_label)
        v3_container_layout.addWidget(self.view_all_players_button, alignment=Qt.AlignLeft)
        
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
        
        
        
        
        
        with open("GUI/HSStyle.qss", "r") as file:
            stylesheet = file.read()
            
            
        self.setLayout(layout)
        self.setStyleSheet(stylesheet)
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec_())
