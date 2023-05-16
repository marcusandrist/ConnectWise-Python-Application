import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
main_win = QMainWindow()
main_win.show()
sys.exit(app.exec_())