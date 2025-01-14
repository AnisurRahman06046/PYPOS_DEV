import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon ,QPixmap # Correct import for QIcon
from PyQt6.QtCore import Qt 
from resource_loader import resource_path



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("POS")
        self.resize(1480, 680)

        # navbar layout
        navBar = QHBoxLayout()

        # Left side: Logo + Navigation buttons
        left_nav = QHBoxLayout()
        logo_label = QLabel()
        load_logo = resource_path("assets/logo.jpg")
        pixmp_logo = QPixmap(load_logo)
        logo_label.setPixmap(pixmp_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        logo_label.setStyleSheet("padding-right:20px")
        left_nav.addWidget(logo_label)

        # Creating the navigation buttons
        self.buttons = {
            "Home": QPushButton("Home"),
            "Orders": QPushButton("Orders"),
            "POS Terminal": QPushButton("POS Terminal"),
            "Products": QPushButton("Products"),
            "Customers": QPushButton("Customers"),
            "Staff": QPushButton("Staff"),
            "Settings": QPushButton("Settings")
        }

        # Default and active styles
        self.default_btn_style = "padding:10px;font-size:25px;border:none;color:black"
        self.active_btn_style = "padding:10px;font-size:25px;border:none;color:blue"

        # Style and connect buttons
        for name, btn in self.buttons.items():
            btn.setStyleSheet(self.default_btn_style)
            btn.clicked.connect(lambda checked, n=name: self.set_active_button(n))
            left_nav.addWidget(btn)

        left_nav.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Right side: Profile
        right_nav = QHBoxLayout()
        profile_logo = QLabel("UserName")
        profile_logo.setStyleSheet("font-size: 20px; padding-right: 10px")
        right_nav.addWidget(profile_logo)

        self.prflBtn = QPushButton()
        load_profile_logo = resource_path("assets/profile.png")
        profilePix = QPixmap(load_profile_logo).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.prflBtn.setIcon(QIcon(profilePix))
        self.prflBtn.setIconSize(profilePix.size())
        self.prflBtn.setStyleSheet(self.default_btn_style)
        right_nav.addWidget(self.prflBtn)
        self.prflBtn.clicked.connect(lambda: self.set_active_button("Profile"))

        navBar.addLayout(left_nav)
        navBar.addLayout(right_nav)

        nav_container = QWidget()
        nav_container.setLayout(navBar)
        nav_container.setStyleSheet("background-color:#FFFFFF; padding:5px")

        # Pages
        self.pages = QStackedWidget()
        pagesTextList = ["Home Page", "Orders Page", "POS Terminal Page", "Products Page", "Customers Page", "Staff Page", "Settings Page", "Profile Page"]

        for c in pagesTextList:
            self.pages.addWidget(self.create_page(c))

        main_layout = QVBoxLayout()
        main_layout.addWidget(nav_container)
        main_layout.addWidget(self.pages)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setStyleSheet("background-color:#e6e7e7")

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
        # Reset all buttons to the default style
        for name, btn in self.buttons.items():
            btn.setStyleSheet(self.default_btn_style)

        # Set the clicked button to the active style
        if active_name in self.buttons:
            self.buttons[active_name].setStyleSheet(self.active_btn_style)

        # Update the stacked widget index
        pages_mapping = list(self.buttons.keys()) + ["Profile"]
        if active_name in pages_mapping:
            self.pages.setCurrentIndex(pages_mapping.index(active_name))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
