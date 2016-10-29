from PyQt5.QtWidgets import QApplication
from UI import UI
from LibraryManager import LibraryManager
import sys

app = QApplication(sys.argv)
ui = UI(LibraryManager())
ui.show()
sys.exit(app.exec_())
