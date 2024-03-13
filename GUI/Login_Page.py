import sys
import os
import pyodbc
import bcrypt
from PyQt5.QtCore import Qt, pyqtSignal
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
    login_Successful = pyqtSignal()
    register = pyqtSignal()
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
        
        self.register_here_button = QPushButton("Click here to register", self)
        self.register_here_button.setObjectName("registerButton")
        self.register_here_button.clicked.connect(self.register_here)   
        
        layout.setContentsMargins(20, 20, 20, 20)  # Adjust as needed
        layout.setSpacing(10)  # Adjust the spacing between widgets
        self.title_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        
        spacer_item = QSpacerItem(0, 20)
        layout.addItem(spacer_item)
        layout.addRow(self.title_label)
        layout.addItem(spacer_item)
        layout.addRow(self.username_edit)      
        layout.addRow(self.password_edit)
        layout.addRow(self.login_button)
        layout.addRow(self.register_here_button)
        
        with open("GUI/login_page.qss", "r") as file:
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
        self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\domus\OneDrive\Desktop\New folder\Database11.accdb;')
        self.cursor = self.conn.cursor()
        
        username = self.username_edit.text()
        password = self.password_edit.text()
        try:
            query = "SELECT * FROM Users WHERE Username = ?"
            self.cursor.execute(query, (username,))
            user = self.cursor.fetchone()

            if user is not None:
             stored_password = user.Password  # Assuming 'Password' is the column name in the database
            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode(), stored_password.encode()):
                QMessageBox.information(self, "Login Successful", "Welcome, {}".format(username))
                self.login_Successful.emit()
                
                return
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        except Exception as e:
            print("Error:", e)
            QMessageBox.critical(self, "Error", "An error occurred. Please try again later.")
    def register_here(self):
        self.register.emit()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
