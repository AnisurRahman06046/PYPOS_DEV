# from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QHBoxLayout,QLineEdit,QComboBox,QListWidget,QPushButton,QLabel,QGridLayout

# from PyQt6.QtGui import QFont,QIcon
# from PyQt6.QtCore import Qt

# class CartWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()

#     def initUi(self):
#         self.main_layout = QVBoxLayout()

#         # first section : search input field, user dropdown and add button
#         search_layout = QHBoxLayout()


#         # search input field
#         self.search_input = QLineEdit()
#         self.search_input.setPlaceholderText("Search by SKU, ID, or Scan")
#         self.search_input.setFont(QFont("Times",14))
#         self.search_input.setStyleSheet("padding:5px;background-color:#F3F3F3;color:black;border:1px solid;border-radius:8px")
#         # self.search_input.setFixedWidth(800)

#         # user dopdown
#         self.user_dropdown = QComboBox()
#         self.user_dropdown.addItem("User 1")
#         self.user_dropdown.addItem("User 2")
#         self.user_dropdown.addItem("User 3")
#         self.user_dropdown.setPlaceholderText("User")
#         # self.user_dropdown.setStyleSheet("padding:5px;background-color:#F3F3F3;color:black;width:200px")


#         # add button 
#         self.add_button = QPushButton("+")
#         self.add_button.setStyleSheet("background-color:blue;")


#         search_layout.addWidget(self.search_input)
#         search_layout.addWidget(self.user_dropdown)
#         search_layout.addWidget(self.add_button)

















#         # second section : table of contents
#         product_list = QListWidget()
#         product_list.addItem("Cart Item 1")
#         product_list.addItem("Cart Item 2")
#         product_list.addItem("Cart Item 3")


#         # third section : payment information : total, vat discount etc
#         payment_info_layout = QHBoxLayout()

#         payment_info_container = QWidget()
#         payment_info_container.setStyleSheet("background-color:#333333;padding:10px;font-weight:bold;font-size:15px;")

#         item_layout = QHBoxLayout()

#         items_label = QLabel("Items")
#         items_amount = QLabel("2")
#         item_layout.addWidget(items_label)
#         item_layout.addWidget(items_amount)
#         item_layout.setStretch(0,2)
#         # item_layout.setStretch(0,2)

#         total_layout = QHBoxLayout()
#         total_label = QLabel("Total")
#         total_amount = QLabel("$100.00")
#         total_layout.addWidget(total_label)
#         total_layout.addWidget(total_amount)
#         total_layout.setStretch(0,2)
        

#         vat_layout = QHBoxLayout()
#         vat_label = QLabel("VAT")
#         vat_amount = QLabel("$20.00")
#         vat_layout.addWidget(vat_label)
#         vat_layout.addWidget(vat_amount)
#         vat_layout.setStretch(0,2)

#         discount_layout = QHBoxLayout()
#         discount_label_button_layout = QVBoxLayout()
#         discount_label = QLabel("Discount")

        
#         discount_type_btn = QComboBox()
#         discount_type_btn.addItem("Percentage")
#         discount_type_btn.addItem("Amount(TK)")
#         discount_input = QLineEdit()
#         discount_label_button_layout.addWidget(discount_label)
#         discount_label_button_layout.addWidget(discount_type_btn)
#         discount_amount = QLabel("$10.00")
#         # discount_layout.addWidget(discount_label)
#         discount_layout.addLayout(discount_label_button_layout)
#         discount_layout.addWidget(discount_type_btn)
#         discount_layout.addWidget(discount_amount)
#         discount_layout.setStretch(0,2)


#         after_discount_layout = QHBoxLayout()
#         after_discount_price = QLabel("After Discount Price")
#         after_discount_price_amount = QLabel("$90.00")
#         after_discount_layout.addWidget(after_discount_price)
#         after_discount_layout.addWidget(after_discount_price_amount)
#         after_discount_layout.setStretch(0,10)
        


#         # after discount and vat layout
#         discount_vat_container = QWidget()
#         discount_vat_container.setStyleSheet("background-color:#333333;padding:10px;font-weight:bold;font-size:15px;")
#         post_discount_price_vat_layout = QVBoxLayout()

#         total_vat_layout = QHBoxLayout()
#         total_vat_price_label = QLabel("Total VAT")
#         total_vat_price_amount = QLabel("$20.00")
#         total_vat_layout.addWidget(total_vat_price_label)
#         total_vat_layout.addWidget(total_vat_price_amount)
#         total_vat_layout.setStretch(0,10)
        




#         post_discount_price_vat_layout.addLayout(after_discount_layout)
#         post_discount_price_vat_layout.addLayout(total_vat_layout)
#         discount_vat_container.setLayout(post_discount_price_vat_layout)

#         # payment_info_layout.addLayout(item_layout)
#         # payment_info_layout.addLayout(toal_layout)
#         # payment_info_layout.addLayout(vat_layout)
#         # payment_info_layout.addLayout(discount_layout)


#         grid =QGridLayout()
#         grid.addLayout(item_layout,0,0)
#         grid.addLayout(total_layout,0,1)
#         grid.addLayout(vat_layout,1,0)
#         grid.addLayout(discount_layout,1,1)
#         payment_info_container.setLayout(grid)
        
#         # grid.setAlignment(Qt.AlignmentFlag.AlignCenter)


#         checkout_button = QPushButton("Checkout")






#         self.main_layout.addLayout(search_layout)
#         self.main_layout.addWidget(product_list)
#         # self.main_layout.addLayout(grid)
#         self.main_layout.addWidget(payment_info_container)
#         # self.main_layout.addLayout(post_discount_price_vat_layout)
#         self.main_layout.addWidget(discount_vat_container)
#         self.setLayout(self.main_layout)



# # app = QApplication([])
# # window = CartWindow()
# # window.show()
# # app.exec()


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

        payment_info_container = QWidget()
        payment_info_container.setStyleSheet("background-color:white;padding:10px;font-weight:bold;font-size:15px;color:black;")

        item_layout = QHBoxLayout()

        items_label = QLabel("Items")
        items_amount = QLabel("2")
        item_layout.addWidget(items_label)
        item_layout.addWidget(items_amount)
        item_layout.setStretch(0,2)
        # item_layout.setStretch(0,2)

        total_layout = QHBoxLayout()
        total_label = QLabel("Total")
        total_amount = QLabel("$100.00")
        total_layout.addWidget(total_label)
        total_layout.addWidget(total_amount)
        total_layout.setStretch(0,2)
        

        vat_layout = QHBoxLayout()
        vat_label = QLabel("VAT")
        vat_amount = QLabel("$20.00")
        vat_layout.addWidget(vat_label)
        vat_layout.addWidget(vat_amount)
        vat_layout.setStretch(0,2)

        discount_layout = QHBoxLayout()
        discount_label_button_layout = QVBoxLayout()
        discount_label = QLabel("Discount")

        discount_btn_input_layout = QHBoxLayout()
        discount_type_btn = QComboBox()
        discount_type_btn.setFixedWidth(130)
        discount_type_btn.addItem("Percentage")
        discount_type_btn.addItem("Amount(TK)")
        # discount_type_btn.setFixedWidth(120)
        discount_input = QLineEdit()
        discount_input.setPlaceholderText("0")
        discount_input.setFixedWidth(50)
        discount_btn_input_layout.addWidget(discount_type_btn)
        discount_btn_input_layout.addWidget(discount_input)
        


        discount_label_button_layout.addWidget(discount_label)
        discount_label_button_layout.addLayout(discount_btn_input_layout)
        discount_amount = QLabel("$10.00")
        discount_amount.setAlignment(Qt.AlignmentFlag.AlignRight)
        # discount_layout.addWidget(discount_label)
        discount_layout.addLayout(discount_label_button_layout)
        # discount_layout.addWidget(discount_type_btn)
        discount_layout.addWidget(discount_amount)
        discount_layout.setStretch(0,2)


        after_discount_layout = QHBoxLayout()
        after_discount_price = QLabel("After Discount Price")
        after_discount_price_amount = QLabel("$90.00")
        after_discount_layout.addWidget(after_discount_price)
        after_discount_layout.addWidget(after_discount_price_amount)
        after_discount_layout.setStretch(0,10)
        


        # after discount and vat layout
        discount_vat_container = QWidget()
        discount_vat_container.setStyleSheet("background-color:#333333;padding:10px;font-weight:bold;font-size:15px;color:white;")
        post_discount_price_vat_layout = QVBoxLayout()

        total_vat_layout = QHBoxLayout()
        total_vat_price_label = QLabel("Total VAT")
        total_vat_price_amount = QLabel("$20.00")
        total_vat_layout.addWidget(total_vat_price_label)
        total_vat_layout.addWidget(total_vat_price_amount)
        total_vat_layout.setStretch(0,10)
        




        post_discount_price_vat_layout.addLayout(after_discount_layout)
        post_discount_price_vat_layout.addLayout(total_vat_layout)
        discount_vat_container.setLayout(post_discount_price_vat_layout)

        # payment_info_layout.addLayout(item_layout)
        # payment_info_layout.addLayout(toal_layout)
        # payment_info_layout.addLayout(vat_layout)
        # payment_info_layout.addLayout(discount_layout)


        grid =QGridLayout()
        grid.addLayout(item_layout,0,0)
        grid.addLayout(total_layout,0,1)
        grid.addLayout(vat_layout,1,0)
        grid.addLayout(discount_layout,1,1)
        payment_info_container.setLayout(grid)
        
        # grid.setAlignment(Qt.AlignmentFlag.AlignCenter)


        checkout_button = QPushButton("Checkout")


        # fourth section : button ,hold,cancel and final price
        payment_control_container = QWidget()
        payment_control_container.setStyleSheet("background-color:#605CA8;padding:10px;font-weight:bold;font-size:15px;color:white;")

        payment_control_layout = QHBoxLayout()
        
        # payment_control_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.final_amount = 3000
        final_price_label = QLabel(f"Total : {self.final_amount}")

        hold_button = QPushButton("Hold")
        hold_button.setStyleSheet("background-color:#FF890F;")
        clear_button = QPushButton("Clear")
        clear_button.setStyleSheet("background-color:#FF0000")
        payment_button = QPushButton("Payment")
        payment_button.setStyleSheet("background-color:#00A65A;")

        payment_control_layout.addWidget(final_price_label)
       
        payment_control_layout.addWidget(hold_button)
        payment_control_layout.addWidget(clear_button)
        payment_control_layout.addWidget(payment_button)

        payment_control_container.setLayout(payment_control_layout)






        self.main_layout.addLayout(search_layout)
        self.main_layout.addWidget(product_list)
        # self.main_layout.addLayout(grid)
        self.main_layout.addWidget(payment_info_container)
        # self.main_layout.addLayout(post_discount_price_vat_layout)
        self.main_layout.addWidget(discount_vat_container)
        self.main_layout.addWidget(payment_control_container)
        self.setLayout(self.main_layout)



# app = QApplication([])
# window = CartWindow()
# window.show()
# app.exec()