from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout,QLabel
from PyQt6.QtCore import Qt


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setGeometry(10,30,1000,600)

        # add title
        # title = QLabel("Login")
        # title.setStyleSheet("font-size: 24px; font-weight: bold")


        # email and login input 
        email = QLineEdit()
        email.setPlaceholderText("Enter your email address")
        email.setFixedWidth(300)
        

        password = QLineEdit()
        password.setPlaceholderText("Enter your password")
        password.setFixedWidth(300)
        password.setEchoMode(QLineEdit.EchoMode.Password)

        # layout.addWidget(title)

        layout.addWidget(email)
        layout.addWidget(password)

        self.setStyleSheet("""
        QLineEdit {
        background-color: #FFFFFF;color:black;text-align:center;border:1px solid;padding:10px;
        border-radius:10px;
        font-size:20px;
        margin-bottom:15px;
        }
        """)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

app = QApplication([])
w = LoginPage()
w.show()
app.exec()