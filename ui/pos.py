from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QListWidget, QGridLayout,QComboBox
)
from PyQt6.QtCore import Qt, QFile, QTextStream,QSize
from PyQt6.QtGui import QFont,QIcon

class PosTerminalPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS Terminal")
        # self.setStyleSheet("background-color:#FFFFFF")
        
        # self.resize(1080, 600)  # Set an initial window size
        # self.setStyleSheet("padding:10px")
        # Create the main grid layout
        grid = QGridLayout()

        # Left section: Product search and product list
        product_section = self.create_product_section()
        product_section.setStyleSheet("padding:10px")
        grid.addWidget(product_section, 0, 0)

        # Right section: Cart
        cart_section = self.create_cart_section()
        grid.addWidget(cart_section, 0, 1)

        # Set column stretch to ensure better resizing
        grid.setColumnStretch(0, 9)  # Left section gets 2 parts
        grid.setColumnStretch(1, 11)  # Right section gets 1 part

        self.setLayout(grid)
    


    def create_product_section(self):
        """Create the left section with search bar and product list."""
        product_section = QWidget()

        product_layout = QVBoxLayout()

        # Search bar
        filter_bar_layout = QHBoxLayout()
        

        # search input field
        # self.search_input = QLineEdit()
        
        # self.search_input.setPlaceholderText("Search by SKU, ID, or Scan")
        # self.search_input.setFont(QFont("Times",14))
        # self.search_input.setStyleSheet("padding:5px;background-color:#F3F3F3;color:black;border:1px solid;border-radius:8px")


        # brand and category
        self.brand = QComboBox()
        self.brand.setPlaceholderText("Brand")
        self.category = QComboBox()
        self.category.setPlaceholderText("Category")

        # clear button
        # clear_btn = QPushButton("Clear")
        # clear_btn.setIcon(QIcon("assets/icons/clr_btn.png"))
        # clear_btn.setFont(QFont("Times",15))
        # clear_btn.setStyleSheet("padding:5px;border:1px solid;border-radius:8px;background-color:#1DA4AF")
        
        # clear_btn.clicked.connect(self.clear_btn_handler)

        # search_bar_layout.addWidget(search_label)
        # search_bar_layout.addWidget(self.search_input)
        # search_bar_layout.addWidget(clear_btn)

        filter_bar_layout.addWidget(self.brand)
        filter_bar_layout.addWidget(self.category)

        # Product list
        product_list = QListWidget()
        product_list.addItem("Product 1")
        product_list.addItem("Product 2")
        product_list.addItem("Product 3")

        # Add components to the layout
        product_layout.addLayout(filter_bar_layout)
        product_layout.addWidget(product_list)

        product_section.setLayout(product_layout)
        return product_section



    def clear_btn_handler(self):
        self.search_input.clear()
    def create_cart_section(self):
        """Create the right section for the cart."""
        cart_section = QWidget()
        cart_layout = QVBoxLayout()

        # Cart title
        cart_title = QLabel("Cart")
        cart_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Cart items (you can use QListWidget or other widgets)
        cart_list = QListWidget()
        cart_list.addItem("Cart Item 1")
        cart_list.addItem("Cart Item 2")

        # Total and Checkout button
        total_label = QLabel("Total: $0.00")
        checkout_button = QPushButton("Checkout")

        cart_layout.addWidget(cart_title)
        cart_layout.addWidget(cart_list)
        cart_layout.addWidget(total_label)
        cart_layout.addWidget(checkout_button)

        cart_section.setLayout(cart_layout)
        return cart_section
    
    def load_stylesheet(self, filename):
        # print(filename)
        # Load the CSS file
        file = QFile(filename)
        if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            self.setStyleSheet(stylesheet)


