# from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel,QGridLayout,QListWidget


# class PosTerminalPage(QWidget):
    
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("POS Terminal")
#         self.resize(800,600)

#         # create the layout for two sections; products and cart section
#         grid = QGridLayout()

#         # left section ; search bar and product lists 
#         product_section = self.create_product_section()
#         grid.addWidget(product_section, 0, 0)

#         # right section ; cart and checkout buttons
#         cart_section = self.create_cart_section()
#         grid.addWidget(cart_section, 0, 1)

#         # set column stretch to ensure better adjustment
#         grid.setColumnStretch(0,2) # left section gets 2 columns
#         grid.setColumnStretch(1,1) # right section gets 1 column

#         self.setLayout(grid)

#         def create_product_section(self):
#             product_section = QWidget()
#             product_layout = QVBoxLayout()

#             # add search bar here
#             search_bar_layout = QHBoxLayout()
#             search_bar_input = QLineEdit()
#             search_bar_input.setPlaceholderText("Search by sku, id or scan")
#             clr_btn = QPushButton("Clear")

#             search_bar_layout.addWidget(search_bar_input)
#             search_bar_layout.addWidget(clr_btn)

#             # product list
#             product_list = QListWidget()
#             product_list.addItem("Product 1")
#             product_list.addItem("Product 2")

#             # adding components to the layout
#             product_layout.addLayout(search_bar_layout)
#             product_layout.addWidget(product_list)

#             product_section.setLayout(product_layout)
#             return product_section
        


#         # create cart section
#         def create_cart_section(self):
#             # right section for the cart
#             # cart_section = QWidget()
#             # cart_layout = QVBoxLayout()
#             pass



from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QListWidget, QGridLayout
)
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QFont

class PosTerminalPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS Terminal")
        # self.setStyleSheet("background-color:#FFFFFF")
        
        self.resize(800, 600)  # Set an initial window size
        
        # Create the main grid layout
        grid = QGridLayout()

        # Left section: Product search and product list
        product_section = self.create_product_section()
        grid.addWidget(product_section, 0, 0)

        # Right section: Cart
        cart_section = self.create_cart_section()
        grid.addWidget(cart_section, 0, 1)

        # Set column stretch to ensure better resizing
        grid.setColumnStretch(0, 2)  # Left section gets 2 parts
        grid.setColumnStretch(1, 1)  # Right section gets 1 part

        self.setLayout(grid)

    def create_product_section(self):
        """Create the left section with search bar and product list."""
        product_section = QWidget()
        product_layout = QVBoxLayout()

        # Search bar
        search_bar_layout = QHBoxLayout()
        # search_label = QLabel("Search Product:")
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search by SKU, ID, or scan")
        search_input.setFont(QFont("Times",14))
        search_button = QPushButton("Search")

        # search_bar_layout.addWidget(search_label)
        search_bar_layout.addWidget(search_input)
        search_bar_layout.addWidget(search_button)

        # Product list
        product_list = QListWidget()
        product_list.addItem("Product 1")
        product_list.addItem("Product 2")
        product_list.addItem("Product 3")

        # Add components to the layout
        product_layout.addLayout(search_bar_layout)
        product_layout.addWidget(product_list)

        product_section.setLayout(product_layout)
        return product_section

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


