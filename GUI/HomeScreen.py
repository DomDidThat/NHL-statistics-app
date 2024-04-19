import sys
import requests
from PyQt5.QtCore import Qt, QFile, QRectF, QByteArray, QUrl
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from shared import top_3_players
from team_stats import top_3_teams



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
        top_3 = top_3_teams()
        top_3_player = top_3_players()
        
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
        
      
        
        response = requests.get(top_3[0]['logo'])
        tp_bytes = QByteArray(response.content)
        tp_renderer = QSvgRenderer(tp_bytes)
        tp_widget = QSvgWidget()
        tp_widget.load(tp_bytes)
        
        
       
        self.tts_label = QLabel("Top Teams")
        self.tts_label.setObjectName("ttsLabel")
        self.tts_label.setAlignment(Qt.AlignLeft)
        self.tts_label.setFixedHeight(50)
        
        self.top_teams_button = QPushButton("Top Teams", self)
        self.top_teams_button.setObjectName("topTeamsButton")
        self.top_teams_button.setFixedSize(100, 35)
        
        
        
        tn1 = QLabel(top_3[0]['Team'])
        tn1.setObjectName("tn1")
        tn1.setFixedHeight(15)
        tn1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        td1 = QLabel(top_3[0]['wins_losses'])
        td1.setObjectName("td1")
        td1.setFixedHeight(15)
        td1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        s3_container = QWidget(l2_container)
        s3_container.setObjectName("s3Container")
        s3_container_layout = QVBoxLayout(s3_container)
        s3_container_layout.setSpacing(0)
        s3_container.setContentsMargins(0, 0, 0, 0)
        
        response = requests.get(top_3[1]['logo'])
        tp2_bytes = QByteArray(response.content)
        tp2_renderer = QSvgRenderer(tp2_bytes)
        tp2_widget = QSvgWidget()
        tp2_widget.load(tp2_bytes)
        tp2_widget.setFixedSize(150, 100)
        
        tn2 = QLabel(top_3[1]['Team'])
        tn2.setObjectName("tn2")
        tn2.setFixedHeight(15)
        tn2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        td2 = QLabel(top_3[1]['wins_losses'])
        td2.setObjectName("td2")
        td2.setFixedHeight(15)
        td2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        s4_container = QWidget(l2_container)
        s4_container.setObjectName("s4Container")
        s4_container_layout = QVBoxLayout(s4_container) 
        s4_container_layout.setSpacing(0)
        s4_container.setContentsMargins(0, 0, 0, 0)
        
        response = requests.get(top_3[2]['logo'])
        tp3_bytes = QByteArray(response.content)
        tp3_renderer = QSvgRenderer(tp2_bytes)
        tp3_widget = QSvgWidget()
        tp3_widget.load(tp3_bytes)
        
        
        tn3 = QLabel(top_3[2]['Team'])
        tn3.setObjectName("tn3")
        tn3.setFixedHeight(15)
        tn3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        td3 = QLabel(top_3[2]['wins_losses'])
        td3.setObjectName("td3")
        td3.setFixedHeight(15)
        td3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
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
        
        
        fp1_url = top_3_player[0]['Picture']
        fp1_image = QImage()
        fp1_image.loadFromData(requests.get(fp1_url).content)
        fp1_pixmap = QPixmap(fp1_image) 
        fp1_pixmap = fp1_pixmap.scaled(300, 150, Qt.KeepAspectRatio)
        fp1_label = QLabel()
        fp1_label.setPixmap(QPixmap(fp1_pixmap))
        fp1_label.show()
        fp1_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp1_name = QLabel(top_3_player[0]['Player'])
        fp1_name.setObjectName("featuredPlayer1")
        fp1_name.setFixedHeight(15)
        fp1_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp1_data = QLabel(top_3_player[0]['Points'])
        fp1_data.setObjectName("featuredPlayer1Data")
        fp1_data.setFixedHeight(15)
        fp1_data.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp2_container = QWidget(l3_container)
        fp2_container.setObjectName("fp2Container")
        fp2_container_layout = QVBoxLayout(fp2_container)
        
        
        fp2_url = top_3_player[1]['Picture']
        fp2_image = QImage()
        fp2_image.loadFromData(requests.get(fp2_url).content)
        fp2_pixmap = QPixmap(fp2_image) 
        fp2_pixmap = fp2_pixmap.scaled(300, 150, Qt.KeepAspectRatio)
        fp2_label = QLabel()
        fp2_label.setPixmap(QPixmap(fp2_pixmap))
        fp2_label.show()
        fp2_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        
        fp2_name = QLabel(top_3_player[1]['Player'])
        fp2_name.setObjectName("featuredPlayer2")
        fp2_name.setFixedHeight(15)
        fp2_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp2_data = QLabel(top_3_player[1]['Points'])
        fp2_data.setObjectName("featuredPlayer2Data")
        fp2_data.setFixedHeight(15)
        fp2_data.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp3_container = QWidget(l3_container)
        fp3_container.setObjectName("fp3Container")
        fp3_container_layout = QVBoxLayout(fp3_container)
        
        fp3_url = top_3_player[2]['Picture']
        fp3_image = QImage()
        fp3_image.loadFromData(requests.get(fp3_url).content)
        fp3_pixmap = QPixmap(fp3_image) 
        fp3_pixmap = fp3_pixmap.scaled(300, 150, Qt.KeepAspectRatio)
        fp3_label = QLabel()
        fp3_label.setPixmap(QPixmap(fp3_pixmap))
        fp3_label.show()
        fp3_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp3_name = QLabel(top_3_player[2]['Player'])
        fp3_name.setObjectName("featuredPlayer3")
        fp3_name.setFixedHeight(15)
        fp3_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        fp3_data = QLabel(top_3_player[2]['Points'])
        fp3_data.setObjectName("featuredPlayer3Data")
        fp3_data.setFixedHeight(15)
        fp3_data.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        
        
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
        
        
        
        
       
        
        s2_container.setFixedSize(200, 175)
        s3_container.setFixedSize(200, 200)
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
        
        s2_container_layout.addWidget(tp_widget)
        s2_container_layout.addSpacing(10)
        s2_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        s2_container_layout.addWidget(tn1)
        s2_container_layout.addWidget(td1)
        
        s3_container_layout.addWidget(tp2_widget)
        s3_container_layout.addSpacing(10)
        s3_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        s3_container_layout.addWidget(tn2)
        s3_container_layout.addWidget(td2)
        
        s4_container_layout.addWidget(tp3_widget)
        s4_container_layout.addSpacing(10)
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
        fp1_container_layout.addWidget(fp1_label)
        fp1_container_layout.addWidget(fp1_name)
        fp1_container_layout.addWidget(fp1_data)
        
        fp2_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        fp2_container_layout.addWidget(fp2_label)
        fp2_container_layout.addWidget(fp2_name)
        fp2_container_layout.addWidget(fp2_data)
        
        fp3_container_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        fp3_container_layout.addWidget(fp3_label)
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
