


from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QFile, QTextStream
from PyQt6.QtGui import QFont

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        login_layout = QVBoxLayout()
        self.setGeometry(800, 300, 1000, 680)

        # Add title
        title = QLabel("Login")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Tahoma", 15))

        # Email and password input
        email = QLineEdit()
        email.setPlaceholderText("Enter your email address")
        email.setFixedWidth(300)

        password = QLineEdit()
        password.setPlaceholderText("Enter your password")
        password.setFixedWidth(300)
        password.setEchoMode(QLineEdit.EchoMode.Password)

        # Login button
        login_button = QPushButton('Login')

        login_layout.addWidget(title)
        login_layout.addWidget(email)
        login_layout.addWidget(password)
        login_layout.addWidget(login_button)

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

app = QApplication([])
w = LoginPage()
w.show()
app.exec()
