import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QPlainTextEdit,
    QMessageBox,
)
from PyQt5.QtCore import QDateTime, QTimer


class CheckInOutApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Employee Dropdown
        self.employee_dropdown = QComboBox(self)
        self.employee_dropdown.setGeometry(100, 50, 200, 30)
        # Load employee names from the API here
        self.employee_dropdown.addItem("Select an employee")
        self.employee_dropdown.addItems(["Employee1", "Employee2", "Employee3"])

        self.employee_dropdown.currentIndexChanged.connect(self.employee_selected)

        # Pin and Confirm Pin fields
        self.pin_input = QLineEdit(self)
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setGeometry(100, 100, 200, 30)
        self.pin_input.hide()

        self.confirm_pin_input = QLineEdit(self)
        self.confirm_pin_input.setEchoMode(QLineEdit.Password)
        self.confirm_pin_input.setGeometry(100, 150, 200, 30)
        self.confirm_pin_input.hide()

        self.submit_pin_button = QPushButton("Submit", self)
        self.submit_pin_button.setGeometry(150, 200, 100, 30)
        self.submit_pin_button.clicked.connect(self.submit_pin)
        self.submit_pin_button.hide()

    def initUI(self):
        # Employee Dropdown
        self.employee_dropdown = QComboBox(self)
        self.employee_dropdown.setGeometry(100, 50, 200, 30)
        # Load employee names from the API here
        self.employee_dropdown.addItems(["Employee1", "Employee2", "Employee3"])
        self.employee_dropdown.setCurrentText("Default Value")

        self.employee_dropdown.currentIndexChanged.connect(self.employee_selected)

        # Pin and Confirm Pin fields
        self.pin_input = QLineEdit(self)
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setGeometry(100, 100, 200, 30)
        self.pin_input.hide()

        self.confirm_pin_input = QLineEdit(self)
        self.confirm_pin_input.setEchoMode(QLineEdit.Password)
        self.confirm_pin_input.setGeometry(100, 150, 200, 30)
        self.confirm_pin_input.hide()

        self.submit_pin_button = QPushButton("Submit", self)
        self.submit_pin_button.setGeometry(150, 200, 100, 30)
        self.submit_pin_button.clicked.connect(self.submit_pin)
        self.submit_pin_button.hide()

    def employee_selected(self, index):
        # Show/hide appropriate fields based on whether the employee is a new user
        # You can determine this using an API call with the selected employee name
        is_new_user = False  # Replace this with the result of your API call

        if is_new_user:
            self.pin_input.show()
            self.confirm_pin_input.show()
        else:
            self.pin_input.show()
            self.confirm_pin_input.hide()

        self.submit_pin_button.show()

    def submit_pin(self):
        # Handle the pin submission logic, verify the pin using the API call
        # You can set the return value of the API call to is_pin_valid
        is_pin_valid = True  # Replace this with the result of your API call

        if is_pin_valid:
            self.show_main_screen()
        else:
            QMessageBox.warning(self, "Error", "Incorrect pin")

    def show_main_screen(self):
        # Hide the pin input fields and show the main screen
        self.employee_dropdown.hide()
        self.pin_input.hide()
        self.confirm_pin_input.hide()
        self.submit_pin_button.hide()

        # Add main screen elements here

        # Show a confirmation message after a successful operation
        QMessageBox.information(
            self,
            "Success",
            "Operation successful. The application will reset in 10 seconds.",
        )
        # Reset the application after 10 seconds
        QTimer.singleShot(10000, self.reset_application)

    def reset_application(self):
        # Reset the application to its initial state
        self.employee_dropdown.show()
        self.pin_input.hide()
        self.confirm_pin_input.hide()
        self.submit_pin_button.hide()

        # Remove main screen elements here

        self.employee_dropdown.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CheckInOutApp()
    ex.setWindowTitle("Check In/Out Application")
    ex.setGeometry(500, 500, 400, 300)
    ex.show()
    sys.exit(app.exec_())
