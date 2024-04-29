import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy
from Login_Page import LoginApp as lp
from RegistrationPage import RegistrationPage as rp
from HomeScreen import HomeScreen as hs
from TeamStatsDialog import TeamStatsDialog
from PlayerStatsDialog import PlayerStatsDialog

class MyApp(QMainWindow):
    def __init__(self):
        """
        Initializes the main window of the NHL Statistics App. This method sets up the window title,
        creates a stacked widget to manage the different application pages (login, registration, home screen),
        and connects signals to the appropriate slots to handle user interactions.
        """
        super().__init__()

        self.setWindowTitle("NHL Statistics App")  # Set the window title
        self.setStyleSheet("Background-color: #FFFFFF")

        self.stacked_widget = QStackedWidget(self)  # Create a stacked widget to manage different pages
        self.setCentralWidget(self.stacked_widget)  # Set the stacked widget as the central widget of the window

        # Initialize the pages of the application
        self.login_page = lp()
        self.registration_page = rp()
        self.home_screen = hs()

        # Set the size policy for each page to Preferred, allowing them to expand and fill available space
        self.login_page.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.registration_page.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.home_screen.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Set a minimum size for each page to ensure they are displayed properly
        self.login_page.setMinimumSize(1, 1)
        self.registration_page.setMinimumSize(1, 1)
        self.home_screen.setMinimumSize(1, 1)

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.registration_page)
        self.stacked_widget.addWidget(self.home_screen)

        # Connect signals from the login and home screen pages to the appropriate slots
        # to handle user actions like logging in, registering, and viewing statistics
        self.login_page.login_Successful.connect(self.show_home_screen)
        self.login_page.register.connect(self.show_registration_page)
        self.home_screen.top_teams_button.clicked.connect(self.show_team_stats_dialog)
        self.home_screen.view_all_players_button.clicked.connect(self.show_player_stats_dialog)

        # Connect the signal for changing the current widget in the stacked widget
        # to adjust the window size accordingly
        self.stacked_widget.currentChanged.connect(self.resizeToCurrentWidget)

        self.show_login_page()  # Show the login page initially
        
    
    def show_team_stats_dialog(self):
        """
        Displays the Team Stats dialog window.

        This method creates an instance of the TeamStatsDialog class and displays it as a modal dialog,
        pausing the execution of any further code in this method until the dialog is closed.
        """
        dialog = TeamStatsDialog()
        dialog.exec_()
        
    def show_player_stats_dialog(self):
        """
        Displays the Player Stats dialog window.

        This method creates an instance of the PlayerStatsDialog class and displays it as a modal dialog,
        pausing the execution of any further code in this method until the dialog is closed. This allows
        the user to interact with the player statistics dialog independently of the main application window.
        """
        dialog = PlayerStatsDialog()
        dialog.exec_()
            
    def show_login_page(self):
        """
        Displays the login page within the application.

        This method sets the current widget of the stacked widget to the login page and then resizes the main window
        to fit the login page's size hint. This ensures that when the login page is shown, it is properly sized and
        displayed to the user.
        """
        self.stacked_widget.setCurrentWidget(self.login_page)  # Set the current widget to the login page
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())  # Resize the window to fit the login page

    def show_registration_page(self):
        """
        Displays the registration page within the application.

        This method sets the current widget of the stacked widget to the registration page and then resizes the main window
        to fit the registration page's size hint. This ensures that when the registration page is shown, it is properly sized
        and displayed to the user. No parameters are required, and the method does not return any values.
        """
        self.stacked_widget.setCurrentWidget(self.registration_page)  # Set the current widget to the registration page
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())  # Resize the window to fit the registration page

    def show_home_screen(self):
        """
        Displays the home screen within the application.

        This method sets the current widget of the stacked widget to the home screen and then resizes the main window
        to fit the home screen's size hint. This ensures that when the home screen is shown, it is properly sized
        and displayed to the user. No parameters are required, and the method does not return any values.
        """
        self.stacked_widget.setCurrentWidget(self.home_screen)  # Set the current widget to the home screen
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())  # Resize the window to fit the home screen
        
    def resizeToCurrentWidget(self, index):
        """
        Resizes the main window to match the size hint of the current widget displayed in the stacked widget.

        This method is called whenever the current widget in the stacked widget changes. It ensures that the main window
        adjusts its size to best fit the size requirements of the currently displayed widget, providing a seamless user
        experience as they navigate through different screens of the application.

        Parameters:
        - index (int): The index of the current widget in the stacked widget.

        Returns:
        - None
        """
        current_widget = self.stacked_widget.widget(index)  # Retrieve the current widget using its index
        if current_widget:
            self.resize(current_widget.sizeHint())  # Resize the main window to the current widget's size hint
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
