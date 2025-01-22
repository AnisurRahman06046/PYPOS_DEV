from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
from PyQt6.QtGui import QIcon,QFont
from PyQt6.QtCore import QSize,Qt
import sys

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700, 300, 1000, 600)
       

        # Create a grid layout
        grid = QGridLayout()

        # Button configurations
        buttons = [
            ("assets/icons/pos.png", "POS Terminal"),
            ("assets/icons/orders.png", "Orders"),
            ("assets/icons/products.png", "Products"),
            ("assets/icons/customers.png", "Customers"),
            ("assets/icons/staffs.png", "Staff"),
            ("assets/icons/settings.png", "Settings"),
            ("assets/icons/regC.png", "Register Close"),
            ("assets/icons/logout.png", "Logout"),
        ]

        # Add buttons to the grid
        for i, (icon_path, text) in enumerate(buttons):
            button = QPushButton()
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(60, 60))
            button.setText(text)
            button.setFont(QFont("Times",15))
            button.setFixedSize(200,200)
            # button.setGeometry(150,200,200,100)
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color:black;
                    border: 1px solid;
                    border-radius: 5px;
                    text-align: center;
                    
                }
                QPushButton:hover {
                    background-color: #dddddd;
                }
                QPushButton::icon {
                    margin-bottom: 10px;
                }
               
            """)
            row = i // 4  # Calculate row (0 or 1)
            col = i % 4   # Calculate column (0 to 3)
            grid.addWidget(button, row, col)

        # Set the layout for the widget
        self.setLayout(grid)
        
