import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy

from Login_Page import LoginApp as lp
from RegistrationPage import RegistrationPage as rp
from HomeScreen import HomeScreen as hs

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NHL Statistics App")
       

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.login_page = lp()
        self.registration_page = rp()
        self.home_screen = hs()

        self.login_page.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.registration_page.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.home_screen.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        self.login_page.setMinimumSize(1, 1)
        self.registration_page.setMinimumSize(1, 1)
        self.home_screen.setMinimumSize(1, 1)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.registration_page)
        self.stacked_widget.addWidget(self.home_screen)

        self.login_page.login_Successful.connect(self.show_home_screen)
        self.login_page.register.connect(self.show_registration_page)

        
        
        self.stacked_widget.currentChanged.connect(self.resizeToCurrentWidget)
        self.show_login_page()

    def show_login_page(self):
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())

    def show_registration_page(self):
        self.stacked_widget.setCurrentWidget(self.registration_page)
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())

    def show_home_screen(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)
        self.resizeToCurrentWidget(self.stacked_widget.currentIndex())

    
    def resizeToCurrentWidget(self, index):
        current_widget = self.stacked_widget.widget(index)
        if current_widget:
            self.resize(current_widget.sizeHint())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
