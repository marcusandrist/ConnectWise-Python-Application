from wrapper import endpoint_get, endpoint_post
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class BarcodeScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Barcode Scanner App")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        start_button = QPushButton("Start Scanning", self)
        start_button.clicked.connect(self.start_scanning)
        layout.addWidget(start_button)

        quit_button = QPushButton("Quit", self)
        quit_button.clicked.connect(self.quit_app)
        layout.addWidget(quit_button)

    def start_scanning(self):
        print("Start scanning barcodes")
        # Here, you can call the capture_barcode() function from the previous example
        # Keep in mind you'll need to modify the function to work with the GUI

    def quit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = BarcodeScannerApp()
    main_win.show()