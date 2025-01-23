# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
# from PyQt6.QtCore import Qt, QFile, QTextStream
# from PyQt6.QtGui import QFont

# class LoginPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         login_layout = QVBoxLayout()
#         self.setGeometry(800, 300, 1000, 680)

#         # Add title
#         title = QLabel("Login")
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         title.setFont(QFont("Tahoma", 15))

#         # Email and password input
#         email = QLineEdit()
#         email.setPlaceholderText("Enter your email address")
#         email.setFixedWidth(300)

#         password = QLineEdit()
#         password.setPlaceholderText("Enter your password")
#         password.setFixedWidth(300)
#         password.setEchoMode(QLineEdit.EchoMode.Password)

#         # Login button
#         login_button = QPushButton('Login')

#         login_layout.addWidget(title)
#         login_layout.addWidget(email)
#         login_layout.addWidget(password)
#         login_layout.addWidget(login_button)

#         # Load CSS from external file
#         self.load_stylesheet("styles/login.qss")
#         # load_stylesheet(self,"styles/login.qss")

#         login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.setLayout(login_layout)

#     def load_stylesheet(self, filename):
#         # Load the CSS file
#         file = QFile(filename)
#         if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
#             stream = QTextStream(file)
#             stylesheet = stream.readAll()
#             self.setStyleSheet(stylesheet)

# app = QApplication([])
# w = LoginPage()
# w.show()
# app.exec()


from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtCore import Qt, QFile, QTextStream
from PyQt6.QtGui import QFont
import requests
from database.database import DatabaseManager

# Initialize database manager
db_manager = DatabaseManager()

class LoginPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent  # Reference to MainWindow
        self.setGeometry(800, 300, 1000, 680)

        login_layout = QVBoxLayout()

        # Add title
        title = QLabel("Login")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Tahoma", 15))

        # Email and password input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email address")
        self.email_input.setFixedWidth(300)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setFixedWidth(300)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Login button
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        login_layout.addWidget(title)
        login_layout.addWidget(self.email_input)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(self.login_button)

        # Load CSS from external file
        self.load_stylesheet("styles/login.qss")

        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(login_layout)

    def load_stylesheet(self, filename):
        # Load the CSS file
        file = QFile(filename)
        if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            self.setStyleSheet(stylesheet)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Email and password cannot be empty.")
            return

        try:
            response = requests.post(
                "https://anzaar-api.bitcommerz.com/api/v1/auth/admin/pos/login",
                json={"email": email, "password": password}
            )
            if response.status_code == 201:
                data = response.json()
                db_manager.save_user_data(data)
                QMessageBox.information(self, "Success", "Login successful.")
                self.parent.show_main_window()
            else:
                QMessageBox.warning(self, "Error", "Invalid credentials.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to the server: {e}")
