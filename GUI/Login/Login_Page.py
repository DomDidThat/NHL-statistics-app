import sys
import os
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFormLayout, QSpacerItem, QSizePolicy

class LoginApp(QWidget):
    """
    A class representing the login page of the NHL Statistics App.

    Attributes:
        title_label (QLabel): The label displaying the title of the app.
        username_edit (QLineEdit): The text input field for the username.
        password_edit (QLineEdit): The text input field for the password.
        login_button (QPushButton): The button to initiate the login process.
        register_here_label (QLabel): The label indicating the option to register.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NHL Statistics App - Login")
        self.setGeometry(100, 100, 440, 400)
        
        self.init_ui()
        
    def init_ui(self):
        """
        Initializes the user interface of the login page.
        """
        layout = QFormLayout()
             
        self.title_label = QLabel("Welcome to the NHL Statistics App", self)                
        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText("Username")      
        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.setObjectName("loginbutton")
        self.login_button.clicked.connect(self.login)
        
        self.register_here_label = QLabel("Click here to register", self)
        self.register_here_label.setObjectName("registerLabel") 
        
        layout.setContentsMargins(20, 20, 20, 20)  # Adjust as needed
        layout.setSpacing(10)  # Adjust the spacing between widgets
        self.title_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.register_here_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        spacer_item = QSpacerItem(0, 20)
        layout.addItem(spacer_item)
        layout.addRow(self.title_label)
        layout.addItem(spacer_item)
        layout.addRow(self.username_edit)      
        layout.addRow(self.password_edit)
        layout.addRow(self.login_button)
        layout.addRow(self.register_here_label)
        
        with open("GUI/Login/login_page.qss", "r") as file:
            stylesheet = file.read()
            
        self.setLayout(layout)
        self.setStyleSheet(stylesheet)

    def login(self):
        """
        Performs the login process by retrieving the entered username and password,
        and validating them against the actual authentication logic.

        If the login is successful, a success message is displayed.
        Otherwise, an error message is displayed.
        """
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Replace the following with your actual authentication logic
        if username == "user" and password == "pass":
            QMessageBox.information(self, "Login Successful", "Welcome, {}".format(username))
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
