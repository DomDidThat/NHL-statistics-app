import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

app = QApplication(sys.argv)

# Get the list of available font families
font_families = QFontDatabase().families()

# Print the list of font families
for font_family in font_families:
    print(font_family)

sys.exit(app.exec_())