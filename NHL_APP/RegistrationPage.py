import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox
import pyodbc
import bcrypt
class RegistrationPage(QWidget):
    def __init__(self):
        """
        Initialize the main window.

        """
        super().__init__()

        self.setWindowTitle("NHL Registration")
        self.setGeometry(100, 100, 400, 600)

        self.init_ui()

    def init_ui(self):
        self.dark_mode = False

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        layout.setSpacing(1)

        # Add a toggle button for dark/light mode in the top right corner
        self.mode_toggle_button = QPushButton("Toggle Mode", self)
        self.mode_toggle_button.setFixedSize(100, 30)
        self.mode_toggle_button.clicked.connect(self.toggle_mode)
        self.mode_toggle_button.setObjectName("toggleButton")
        layout.addWidget(self.mode_toggle_button, alignment=Qt.AlignRight)

        # Add the title 
        self.title_label = QLabel("NHL Registration", self)
        
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        
        form_layout = QFormLayout()
        form_layout.setSpacing(5)
        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText("Username")

        self.email_edit = QLineEdit(self)
        self.email_edit.setPlaceholderText("Email")
         
        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.confirm_password_edit = QLineEdit(self)
        self.confirm_password_edit.setPlaceholderText("Confirm Password")
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.register_user)
        self.register_button.setObjectName("registerButton")
        form_layout.setContentsMargins(50, 0, 50, 50)  
        form_layout.addRow(self.username_edit)
        form_layout.addRow(self.email_edit)
        form_layout.addRow(self.password_edit)
        form_layout.addRow(self.confirm_password_edit)
        form_layout.addRow(self.register_button)

        layout.addLayout(form_layout)

        self.setLayout(layout)

        # Load stylesheet from external file
        self.load_stylesheet()           
            # Load stylesheet from external file

    def toggle_mode(self):
        """
        Toggle between dark and light mode.

        """
        self.dark_mode = not self.dark_mode
        self.load_stylesheet()

    def load_stylesheet(self):
        """
        Load the stylesheet for the GUI.

        """
        stylesheet_file = "NHL_APP//styles_dark.qss" if self.dark_mode else "NHL_APP//styles_light.qss"
        with open(stylesheet_file, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def register_user(self):
        """
        Register a new user.

        """
        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=C:\\Users\\domus\\OneDrive - Hillsborough Community College\\Desktop\\DB\\Database21.accdb"
        )
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

        username = self.username_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()
        
        # Validate registration data
        if not username or not email or not password:
            QMessageBox().warning(self, "Registration", "Please fill in all fields.")
            return

        if password!= confirm_password:
            QMessageBox().warning(self, "Registration", "Passwords do not match!")
            return
        
        if len(password) < 8:
            QMessageBox().warning(self, "Registration", "Password must be at least 8 characters long.")
            return

        # Hash the password securely before storing it
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        try:
            #check if the email already exists in the database
            query = "SELECT * FROM Users WHERE Email = ?"
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()
            if result[0] > 0:
                QMessageBox().warning(self, "Registration", "Email already exists!")
                return
            # Insert the user data into the database
            query = "INSERT INTO Users (Username, Email, Password) VALUES (?,?,?)"
            self.cursor.execute(query, (username, email, hashed_password))
            self.conn.commit()

            # Clear the input fields
            self.username_edit.clear()
            self.email_edit.clear()
            self.password_edit.clear()
            self.confirm_password_edit.clear()

            # Display a success message
            QMessageBox().information(self, "Registration", "User registered successfully!")
        except pyodbc.Error as e:
            QMessageBox().critical(self, "Registration Error", f"An error occurred: {str(e)}")
        except Exception as e:
            QMessageBox().critical(self, "Registration Error", f"An unexpected error occurred: {str(e)}")

    def closeEvent(self, event):
        """
        Close the database connection when the window is closed.

        """
        # Close the database connection when the window is closed
        self.conn.close()           
                # Load stylesheet from external file
            
            

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_page = RegistrationPage()
    registration_page.show()
    sys.exit(app.exec_())
