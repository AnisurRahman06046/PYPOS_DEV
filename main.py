import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget,
    QStackedWidget, QLineEdit, QMessageBox, QSizePolicy,QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import sqlite3
from resource_loader import resource_path
import requests
from ui.products import ProductPage
from ui.orders import OrderPage
from ui.home import HomePage
from ui.customers import CustomerPage
from ui.staffs import StaffPage
from ui.settings import SettingsPage
from ui.pos import PosTerminalPage


# Database setup
def create_database():
    conn = sqlite3.connect("local_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            gender TEXT,
            status TEXT,
            access_token TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_user_data():
    conn = sqlite3.connect("local_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    conn.close()
    return user

def save_user_data(user_data):
    conn = sqlite3.connect("local_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (id, first_name, last_name, email, phone, gender, status, access_token)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_data['user']['id'],
        user_data['user']['firstName'],
        user_data['user']['lastName'],
        user_data['user']['email'],
        user_data['user']['phone'],
        user_data['user']['gender'],
        user_data['user']['status'],
        user_data['access_token']
    ))
    conn.commit()
    conn.close()

def clear_user_data():
    conn = sqlite3.connect("local_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    
    
    
# Login Page
class LoginPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Login")
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Email and password cannot be empty.")
            return

        try:
            response = requests.post("https://anzaar-api.bitcommerz.com/api/v1/auth/admin/pos/login", json={"email": email, "password": password})
            if response.status_code == 201:
                data = response.json()
                save_user_data(data)
                QMessageBox.information(self, "Success", "Login successful.")
                self.parent.show_main_window()
            else:
                QMessageBox.warning(self, "Error", "Invalid credentials.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to the server: {e}")




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS")
        self.resize(1480, 680)
        self.navBar = None
        self.pages = None
        self.user_name_label = None
        self.logout_button = None
        self.buttons = {}
        self.init_ui()
        user = get_user_data()
        if not user:
            self.show_login_page()

    def init_ui(self):
        self.navBar = QHBoxLayout()

        # Left navigation section (logo and buttons)
        left_nav = QHBoxLayout()
        logo_label = QLabel()
        pixmp_logo = QPixmap(resource_path("assets/logo.png"))
        logo_label.setPixmap(pixmp_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        logo_label.setStyleSheet("padding-right:20px")
        left_nav.addWidget(logo_label)

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

        # Add a spacer to push the right nav to the far right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        left_nav.addWidget(spacer)

        # Right navigation section (profile and dropdown)
        right_nav = QHBoxLayout()

        self.profile_logo = QLabel()
        pixmp_profile = QPixmap(resource_path("assets/profile.png"))
        self.profile_logo.setPixmap(pixmp_profile.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.profile_logo.setStyleSheet("margin-right:10px;")
        self.profile_logo.mousePressEvent = self.toggle_profile_info  # Set the click event for profile logo
        right_nav.addWidget(self.profile_logo)

        # Create a floating dropdown menu
        self.profile_dropdown = QWidget(None)  # Independent floating widget
        self.profile_dropdown.setWindowFlags(Qt.WindowType.Popup)  # Ensures it behaves like a dropdown
        self.profile_dropdown.setStyleSheet(
            """
            background-color: white;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
            """
        )
        profile_dropdown_layout = QVBoxLayout()
        self.user_name_label = QLabel("Guest")
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        profile_dropdown_layout.addWidget(self.user_name_label)
        profile_dropdown_layout.addWidget(self.logout_button)
        self.profile_dropdown.setLayout(profile_dropdown_layout)

        self.navBar.addLayout(left_nav)
        self.navBar.addLayout(right_nav)

        nav_container = QWidget()
        nav_container.setLayout(self.navBar)

        self.pages = QStackedWidget()
        for page_name in self.buttons.keys():
            if page_name =="Orders":
                self.pages.addWidget(OrderPage())
            elif page_name =="Products":
                self.pages.addWidget(ProductPage())
            elif page_name=="Home":
                self.pages.addWidget(HomePage())
            elif page_name=="Customers":
                self.pages.addWidget(CustomerPage())
            elif page_name =="Staff":
                self.pages.addWidget(StaffPage())
            elif page_name=="Settings":
                self.pages.addWidget(SettingsPage())
            elif page_name=="POS Terminal":
                self.pages.addWidget(PosTerminalPage())
            else:
                # page = QLabel(f"Welcome to {page_name}")
                # page.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.pages.addWidget(HomePage())

        main_layout = QVBoxLayout()
        main_layout.addWidget(nav_container)
        main_layout.addWidget(self.pages)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def toggle_profile_info(self, event):
        """Toggles the visibility of the dropdown with the user's name and logout button."""
        if not self.profile_dropdown.isVisible():
            # Calculate the global position of the profile logo
            global_pos = self.profile_logo.mapToGlobal(self.profile_logo.rect().bottomLeft())
            self.profile_dropdown.move(global_pos)
            self.profile_dropdown.setVisible(True)
        else:
            self.profile_dropdown.setVisible(False)

    def show_login_page(self):
        self.login_page = LoginPage(self)
        self.setCentralWidget(self.login_page)

    def show_main_window(self):
        self.init_ui()
        self.update_user_info()  # Update the username after initializing the UI

    def update_user_info(self):
        user = get_user_data()
        if user:
            user_name = f"{user[1]} {user[2]}"  # first_name and last_name
            self.user_name_label.setText(user_name)
        else:
            self.user_name_label.setText("Guest")

    def set_active_button(self, active_name):
        for name, btn in self.buttons.items():
            btn.setStyleSheet(self.default_btn_style)
        self.buttons[active_name].setStyleSheet(self.active_btn_style)
        self.pages.setCurrentIndex(list(self.buttons.keys()).index(active_name))

    def logout(self):
        confirm = QMessageBox.question(
            self,
            "Confirm Logout",
            "Are you sure you want to log out?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            clear_user_data()
            self.show_login_page()

# App Execution
if __name__ == "__main__":
    create_database()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())