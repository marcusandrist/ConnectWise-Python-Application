import typing
from PyQt5 import QtCore
from wrapper import endpoint_get, endpoint_post
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

# Subclass for QMainWindow 
class ScannerApp(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Window settings
        self.setWindowTitle("Tool Checkout v0.1.0")
        self.setWindowIcon(QIcon("tool_checkout.png"))
        self.resize(600, 600)

        # Set CSS (to-do)
        # self.load_stylesheet('styles.css')

        # Execute application inside GUI
        self.app()

    def app(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = ScannerApp()
    main_win.show()
    sys.exit(app.exec_())