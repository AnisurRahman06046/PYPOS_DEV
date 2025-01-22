# from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QGridLayout
# from PyQt6.QtGui import QIcon
# from PyQt6.QtCore import QSize 
# class HomePage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(100,100,600,400)


#         grid = QGridLayout()

#         button1  = QPushButton()
#         button1.setIcon(QIcon("assets/icons/pos.png"))
#         button1.setIconSize(QSize(48,48))
#         button1.setText("POS Terminal")
#         button1.setStyleSheet("""
#             QPushButton{
#             background-color:white;
#             text-align:center;
#             height:100px;
#             width:100px;
#             flex-direction:column;
#             }
#         """)

#         button2  = QPushButton()

#         button2.setIcon(QIcon("assets/icons/orders.png"))
#         button2.setIconSize(QSize(48,48))
#         button2.setText("Orders")
#         button2.setStyleSheet("""
#             QPushButton{
#             background-color:white;
#             text-align:center;
#             height:100px;
#             width:100px;
#             flex-direction:column;
#             """)
        
#         button3  = QPushButton()
#         button3.setIcon(QIcon("assets/icons/products.png"))
#         button3.setIconSize(QSize(48,48))
#         button3.setText("Products")
#         button3.setStyleSheet("""
#             QPushButton{
#             background-color:white;
#             text-align:center;
#             height:100px;
#             width:100px;
#             flex-direction:column;
#             """)
        
#         button4  = QPushButton()
#         button4.setIcon(QIcon("assets/icons/customers.png"))
#         button4.setIconSize(QSize(48,48))
#         button4.setText("Customers")
#         button4.setStyleSheet("""
#             QPushButton{
#             background-color:white;
#             text-align:center;
#             height:100px;
#             width:100px;
#             flex-direction:column;
#             """)
        
#         button5  = QPushButton()
#         button5.setIcon(QIcon("assets/icons/reports.png"))
#         button5.setIconSize(QSize(48,48))
#         button5.setText("Reports")
#         button5.setStyleSheet("""
#             QPushButton{
#             background-color:white;
#             text-align:center;
#             height:100px;
#             width:100px;
#             flex-direction:column;
#             """)

        
        


from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
from PyQt6.QtGui import QIcon,QFont
from PyQt6.QtCore import QSize,Qt
import sys

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Home Page")

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
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    text-align: bottom;
                    height: 80px;
                    width: 80px;
                    color:black;
                  
                  
                }
                QPushButton:hover {
                    background-color: #dddddd;
                }
               
            """)
            row = i // 4  # Calculate row (0 or 1)
            col = i % 4   # Calculate column (0 to 3)
            grid.addWidget(button, row, col)

        # Set the layout for the widget
        self.setLayout(grid)
        
