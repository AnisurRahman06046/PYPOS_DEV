import sys
import sqlite3
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QWidget, QStackedWidget, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt


class Database:
    def __init__(self, db_name="app.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_user_table()

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            token TEXT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_user(self, email, token):
        query = "INSERT INTO user (email, token) VALUES (?, ?)"
        self.cursor.execute(query, (email, token))
        self.conn.commit()

    def get_user(self):
        query = "SELECT * FROM user LIMIT 1"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def clear_user(self):
        query = "DELETE FROM user"
        self.cursor.execute(query)
        self.conn.commit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()

        # Check if user is logged in
        user = self.db.get_user()
        if user:
            self.init_main_ui()
        else:
            self.init_login_ui()

    def init_login_ui(self):
        self.setWindowTitle("Login")
        login_widget = QWidget()
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        login_widget.setLayout(layout)
        self.setCentralWidget(login_widget)

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # Call the login API
        response = self.call_login_api(email, password)
        if response and response.get("token"):
            # Save user details in the database
            self.db.clear_user()  # Clear previous user data
            self.db.insert_user(email, response["token"])
            QMessageBox.information(self, "Login", "Login successful!")
            self.init_main_ui()  # Switch to the main UI
        else:
            QMessageBox.warning(self, "Login", "Invalid credentials!")

    def call_login_api(self, email, password):
        try:
            url = "https://anzaar-api.bitcommerz.com/api/v1/auth/admin/pos/login"  # Replace with your API endpoint
            payload = {"email": email, "password": password}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"API Error: {e}")
        return None

    def init_main_ui(self):
        self.setWindowTitle("POS")
        self.resize(1480, 680)

        # Clear the existing central widget
        if self.centralWidget():
            self.centralWidget().deleteLater()

        # Navbar layout
        navBar = QHBoxLayout()
        left_nav = QHBoxLayout()
        logo_label = QLabel()
        # Replace with your actual resource loader
        pixmp_logo = QPixmap("assets/logo.jpg")
        logo_label.setPixmap(pixmp_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        left_nav.addWidget(logo_label)

        # Creating buttons
        self.buttons = {
            "Home": QPushButton("Home"),
            "Orders": QPushButton("Orders"),
            "POS Terminal": QPushButton("POS Terminal"),
            "Products": QPushButton("Products"),
            "Customers": QPushButton("Customers"),
            "Staff": QPushButton("Staff"),
            "Settings": QPushButton("Settings")
        }

        self.default_btn_style = "padding:10px;font-size:25px;border:none;color:black"
        self.active_btn_style = "padding:10px;font-size:25px;border:none;color:blue"

        for name, btn in self.buttons.items():
            btn.setStyleSheet(self.default_btn_style)
            btn.clicked.connect(lambda checked, n=name: self.set_active_button(n))
            left_nav.addWidget(btn)

        left_nav.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Pages setup
        self.pages = QStackedWidget()
        for c in self.buttons.keys():
            self.pages.addWidget(self.create_page(f"{c} Page"))

        main_layout = QVBoxLayout()
        main_layout.addLayout(navBar)
        main_layout.addWidget(self.pages)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Set the default active button to "Home"
        self.set_active_button("Home")

    def create_page(self, text):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def set_active_button(self, active_name):
        for name, btn in self.buttons.items():
            btn.setStyleSheet(self.default_btn_style)

        if active_name in self.buttons:
            self.buttons[active_name].setStyleSheet(self.active_btn_style)

        self.pages.setCurrentIndex(list(self.buttons.keys()).index(active_name))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
