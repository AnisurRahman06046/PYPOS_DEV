# from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
# from PyQt6.QtGui import QIcon,QFont
# from PyQt6.QtCore import QSize,Qt
# import sys
# from resource_loader import resource_path
# class HomePage(QWidget):
#     def __init__(self):
#         super().__init__()
#         # self.setGeometry(700, 300, 1000, 600)
       

#         # Create a grid layout
#         grid = QGridLayout()

#         # Button configurations
#         buttons = [
#             ("assets/pos.png", "POS Terminal"),
#             ("assets/orders.png", "Orders"),
#             ("assets/products.png", "Products"),
#             ("assets/customers.png", "Customers"),
#             ("assets/staffs.png", "Staff"),
#             ("assets/settings.png", "Settings"),
#             ("assets/regC.png", "Register Close"),
#             ("assets/logout.png", "Logout"),
#         ]

#         # Add buttons to the grid
#         for i, (icon_path, text) in enumerate(buttons):
#             button = QPushButton()
#             button.setIcon(QIcon(resource_path(icon_path)))
#             button.setIconSize(QSize(60, 60))
#             button.setText(text)
#             button.setFont(QFont("Times",15))
#             button.setFixedSize(200,200)
#             # button.setGeometry(150,200,200,100)
#             button.setStyleSheet("""
#                 QPushButton {
#                     background-color: white;
#                     color:black;
#                     border: 1px solid;
#                     border-radius: 5px;
#                     text-align: center;
                    
#                 }
#                 QPushButton:hover {
#                     background-color: #dddddd;
#                 }
#                 QPushButton::icon {
#                     margin-bottom: 10px;
#                 }
               
#             """)
#             row = i // 4  # Calculate row (0 or 1)
#             col = i % 4   # Calculate column (0 to 3)
#             grid.addWidget(button, row, col)

#         # Set the layout for the widget
#         self.setLayout(grid)
        

from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize, Qt
from resource_loader import resource_path


class HomePage(QWidget):
    def __init__(self, navigate_to_page_callback):
        super().__init__()
        self.navigate_to_page = navigate_to_page_callback  # Callback function to navigate

        # Create a grid layout
        grid = QGridLayout()

        # Button configurations
        buttons = [
            ("assets/pos.png", "POS Terminal"),
            ("assets/orders.png", "Orders"),
            ("assets/products.png", "Products"),
            ("assets/customers.png", "Customers"),
            ("assets/staffs.png", "Staff"),
            ("assets/settings.png", "Settings"),
            ("assets/regC.png", "Register Close"),
            ("assets/logout.png", "Logout"),
        ]

        # Add buttons to the grid
        for i, (icon_path, text) in enumerate(buttons):
            button = QPushButton()
            button.setIcon(QIcon(resource_path(icon_path)))
            button.setIconSize(QSize(60, 60))
            button.setText(text)
            button.setFont(QFont("Times", 15))
            button.setFixedSize(200, 200)
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border: 1px solid;
                    border-radius: 5px;
                    text-align: center;
                }
                QPushButton:hover {
                    background-color: #dddddd;
                }
            """)
            button.clicked.connect(lambda checked, page=text: self.navigate_to_page(page))  # Link button to navigation
            row = i // 4  # Calculate row (0 or 1)
            col = i % 4   # Calculate column (0 to 3)
            grid.addWidget(button, row, col)

        # Set the layout for the widget
        self.setLayout(grid)
