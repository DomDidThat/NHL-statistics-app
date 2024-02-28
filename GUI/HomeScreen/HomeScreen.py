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
        self.setGeometry(100, 100, 1920, 1080)

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
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        l2_container = QWidget(self)
        l2_container.setObjectName("l2Container")
        l2_container_layout = QVBoxLayout(l2_container)

        self.tts_label = QLabel("Top Teams")
        self.tts_label.setObjectName("ttsLabel")
        self.tts_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.tts_label.setFixedHeight(50)
        
        self.top_teams_button = QPushButton("Top Teams", self)
        self.top_teams_button.setObjectName("topTeamsButton")
        self.top_teams_button.setFixedSize(100, 35)
        

        l1_container.setFixedSize(1920, 200)
        l2_container.setFixedSize(1920, 200)
        
        l1_container_layout.addWidget(self.title_label)
        l1_container_layout.addWidget(self.l1)
        l1_container_layout.addWidget(self.get_started_button, alignment=Qt.AlignCenter | Qt.AlignTop)

        l2_container_layout.addWidget(self.tts_label)
        layout.addItem(spacer_item)
        l2_container_layout.addWidget(self.top_teams_button, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(l1_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(l2_container, alignment=Qt.AlignCenter | Qt.AlignTop)
        
        with open("GUI/HomeScreen/HSStyle.qss", "r") as file:
            stylesheet = file.read()
            
            
        self.setLayout(layout)
        self.setStyleSheet(stylesheet)
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec_())
