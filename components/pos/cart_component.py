from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QHBoxLayout,QLineEdit,QComboBox,QListWidget,QPushButton,QLabel,QGridLayout

from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import Qt

class CartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.main_layout = QVBoxLayout()

        # first section : search input field, user dropdown and add button
        search_layout = QHBoxLayout()


        # search input field
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by SKU, ID, or Scan")
        self.search_input.setFont(QFont("Times",14))
        self.search_input.setStyleSheet("padding:5px;background-color:#F3F3F3;color:black;border:1px solid;border-radius:8px")
        # self.search_input.setFixedWidth(800)

        # user dopdown
        self.user_dropdown = QComboBox()
        self.user_dropdown.addItem("User 1")
        self.user_dropdown.addItem("User 2")
        self.user_dropdown.addItem("User 3")
        self.user_dropdown.setPlaceholderText("User")
        # self.user_dropdown.setStyleSheet("padding:5px;background-color:#F3F3F3;color:black;width:200px")


        # add button 
        self.add_button = QPushButton("+")
        self.add_button.setStyleSheet("background-color:blue;")


        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.user_dropdown)
        search_layout.addWidget(self.add_button)

















        # second section : table of contents
        product_list = QListWidget()
        product_list.addItem("Cart Item 1")
        product_list.addItem("Cart Item 2")
        product_list.addItem("Cart Item 3")


        # third section : payment information : total, vat discount etc
        payment_info_layout = QHBoxLayout()

        item_layout = QHBoxLayout()

        items_label = QLabel("Items")
        items_amount = QLabel("2")
        item_layout.addWidget(items_label)
        item_layout.addWidget(items_amount)

        toal_layout = QHBoxLayout()
        total_label = QLabel("Total")
        total_amount = QLabel("$100.00")
        toal_layout.addWidget(total_label)
        toal_layout.addWidget(total_amount)

        vat_layout = QHBoxLayout()
        vat_label = QLabel("VAT")
        vat_amount = QLabel("$20.00")
        vat_layout.addWidget(vat_label)
        vat_layout.addWidget(vat_amount)

        discount_layout = QHBoxLayout()
        discount_label = QLabel("Discount")
        discount_amount = QLabel("$10.00")
        discount_layout.addWidget(discount_label)
        discount_layout.addWidget(discount_amount)


        after_discount_layout = QHBoxLayout()
        after_discount_price = QLabel("After Discount Price")
        after_discount_price_amount = QLabel("$90.00")
        after_discount_layout.addWidget(after_discount_price)
        after_discount_layout.addWidget(after_discount_price_amount)


        # after discount and vat layout
        post_discount_price_vat_layout = QVBoxLayout()

        total_vat_layout = QHBoxLayout()
        total_vat_price = QLabel("Total VAT")
        total_vat_price_amount = QLabel("$20.00")
        total_vat_layout.addWidget(total_vat_price)
        total_vat_layout.addWidget(total_vat_price_amount)




        post_discount_price_vat_layout.addLayout(after_discount_layout)
        post_discount_price_vat_layout.addLayout(total_vat_layout)

        # payment_info_layout.addLayout(item_layout)
        # payment_info_layout.addLayout(toal_layout)
        # payment_info_layout.addLayout(vat_layout)
        # payment_info_layout.addLayout(discount_layout)


        grid =QGridLayout()
        grid.addLayout(item_layout,0,0)
        grid.addLayout(toal_layout,0,1)
        grid.addLayout(vat_layout,1,0)
        grid.addLayout(discount_layout,1,1)
        
        # grid.setAlignment(Qt.AlignmentFlag.AlignCenter)


        checkout_button = QPushButton("Checkout")






        self.main_layout.addLayout(search_layout)
        self.main_layout.addWidget(product_list)
        self.main_layout.addLayout(grid)
        self.main_layout.addLayout(post_discount_price_vat_layout)
        self.setLayout(self.main_layout)



# app = QApplication([])
# window = CartWindow()
# window.show()
# app.exec()