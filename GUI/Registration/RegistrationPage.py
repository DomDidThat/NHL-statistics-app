import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout


class RegistrationPage(QWidget):
    def __init__(self):
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
        self.load_stylesheet()

    def toggle_mode(self):
        self.dark_mode = not self.dark_mode
        self.load_stylesheet()

    def load_stylesheet(self):
        stylesheet_file = "GUI/Registration/styles_dark.qss" if self.dark_mode else "GUI/Registration/styles_light.qss"
        with open(stylesheet_file, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_page = RegistrationPage()
    registration_page.show()
    sys.exit(app.exec_())