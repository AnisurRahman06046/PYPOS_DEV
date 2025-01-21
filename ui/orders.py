# from PyQt6.QtWidgets import QWidget,QVBoxLayout,QTableWidget,QMessageBox,QTableWidgetItem
# from utils.get_token import getToken
# import requests
# class OrderPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout= QVBoxLayout()
#         # create table widget to display orders
#         self.orders_table = QTableWidget()
#         self.orders_table.setColumnCount(6)
#         self.orders_table.setHorizontalHeaderLabels(["ID","Order Date","Customer Name","Customer Phone","Discount Type","Discount Value","Total Price"])
#         self.orders_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
#         layout.addWidget(self.orders_table)
#         self.setLayout(layout)
#         self.fetch_orders()
    
#     def fetch_orders(self):
#         try:
#             token = getToken()
#             # print(f'{token}')
#             if not token:
#                 QMessageBox.warning(self,"Error","Unauthenticated")
#                 return 
#             headers = {"Authorization":f"Bearer {token}"}
#             res = requests.get("https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos", headers=headers)
#             # print(res.json())
#             if res.status_code==200:
#                 orders = res.json()
#                 self.populate_orders_table(orders)
#             else:
#                 QMessageBox.warning(self,"Error","Failed to fetch data")
            
#         except Exception as e:
#             QMessageBox.warning(self,"Error",f'{e}')
#             print(f'{e}')

#     def populate_orders_table(self,orders):
#         self.orders_table.setRowCount(len(orders))

#         for row_idx,order in enumerate(orders):
#             self.orders_table.setItem(row_idx,0,QTableWidgetItem(str(order.get("id",""))))
#             self.orders_table.setItem(row_idx,1,QTableWidgetItem(str(order.get("createdAt",""))))
#             self.orders_table.setItem(row_idx,2,QTableWidgetItem(order.get("customer_name"," ")))
#             self.orders_table.setItem(row_idx,3,QTableWidgetItem(order.get("customer_phone","")))
#             self.orders_table.setItem(row_idx,4,QTableWidgetItem(order.get("discountType","")))
#             self.orders_table.setItem(row_idx,5,QTableWidgetItem(str(order.get("discountAmount",""))))
#             self.orders_table.setItem(row_idx,6,QTableWidgetItem(str(order.get("grandTotal",""))))
#     # def init_ui(self):
#     #     layout = QVBoxLayout()
#     #     title_lable = QLabel("Order no 1234")
#     #     layout.addWidget(title_lable)
#     #     self.setLayout(layout)





# updated code for date formatting and table style

# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
# )
# from PyQt6.QtCore import Qt
# from datetime import datetime
# import requests

# # Replace with your actual implementation of getToken
# from utils.get_token import getToken


# class OrderPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
        
#         # Create table widget to display orders
#         self.orders_table = QTableWidget()
#         self.orders_table.setColumnCount(7)  # Adjust column count if necessary
#         self.orders_table.setHorizontalHeaderLabels(
#             [
#                 "ID",
#                 "Order Date",
#                 "Customer Name",
#                 "Customer Phone",
#                 "Discount Type",
#                 "Discount Value",
#                 "Total Price",
#             ]
#         )
#         self.orders_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Make columns stretch to fit the window
#         self.orders_table.horizontalHeader().setStretchLastSection(True)
#         self.orders_table.horizontalHeader().setSectionResizeMode(
#             QHeaderView.ResizeMode.Stretch
#         )

#         layout.addWidget(self.orders_table)
#         self.setLayout(layout)

#         # Maximize the window
#         self.setWindowState(Qt.WindowState.WindowMaximized)

#         self.fetch_orders()

#     def fetch_orders(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return
#             headers = {"Authorization": f"Bearer {token}"}
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos",
#                 headers=headers,
#             )
#             if res.status_code == 200:
#                 orders = res.json()
#                 self.populate_orders_table(orders)
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", f"{e}")
#             print(f"{e}")

#     def populate_orders_table(self, orders):
#         self.orders_table.setRowCount(len(orders))

#         for row_idx, order in enumerate(orders):
#             # Parse and format the createdAt field
#             created_at = order.get("createdAt", "")
#             if created_at:
#                 try:
#                     # Remove milliseconds if present
#                     created_at = created_at.split(".")[0]  # Keeps only "2024-04-17T02:40:03"
#                     date_obj = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S")
#                     formatted_date = date_obj.strftime("%m/%d/%Y, %I:%M:%S %p")
#                 except ValueError:
#                     formatted_date = created_at  # Use original value if parsing fails
#             else:
#                 formatted_date = ""

#             self.orders_table.setItem(row_idx, 0, QTableWidgetItem(str(order.get("id", ""))))
#             self.orders_table.setItem(row_idx, 1, QTableWidgetItem(formatted_date))
#             self.orders_table.setItem(row_idx, 2, QTableWidgetItem(order.get("customer_name", " ")))
#             self.orders_table.setItem(row_idx, 3, QTableWidgetItem(order.get("customer_phone", "")))
#             self.orders_table.setItem(row_idx, 4, QTableWidgetItem(order.get("discountType", "")))
#             self.orders_table.setItem(row_idx, 5, QTableWidgetItem(str(order.get("discountAmount", ""))))
#             self.orders_table.setItem(row_idx, 6, QTableWidgetItem(str(order.get("grandTotal", ""))))


# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
#     QHBoxLayout,
#     QPushButton,
#     QLabel,
#     QSpacerItem,
#     QSizePolicy
# )
# from PyQt6.QtCore import Qt
# from datetime import datetime
# import requests
# from utils.get_token import getToken

# class OrderPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Pagination variables
#         self.current_page = 1
#         self.rows_per_page = 10
#         self.all_orders = []  # Store all orders fetched from the API

#         layout = QVBoxLayout()

#         # Create table widget to display orders
#         self.orders_table = QTableWidget()
#         self.orders_table.setColumnCount(7)  # Adjust column count if necessary
#         self.orders_table.setHorizontalHeaderLabels(
#             [
#                 "ID",
#                 "Order Date",
#                 "Customer Name",
#                 "Customer Phone",
#                 "Discount Type",
#                 "Discount Value",
#                 "Total Price",
#             ]
#         )
#         self.orders_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Make columns stretch to fit the window
#         self.orders_table.horizontalHeader().setStretchLastSection(True)
#         self.orders_table.horizontalHeader().setSectionResizeMode(
#             QHeaderView.ResizeMode.Stretch
#         )

#         # Add the table to the layout
#         layout.addWidget(self.orders_table)

#         # Create navigation buttons (Previous, Next)
#         self.navigation_layout = QHBoxLayout()

#         # Styling smaller buttons
#         self.prev_button = QPushButton("<")
#         self.prev_button.setFixedSize(30, 30)
#         self.page_label = QLabel("Page 1 of 1")
#         self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.next_button = QPushButton(">")
#         self.next_button.setFixedSize(30, 30)

#         # Add spacer items to center the buttons around the page number
#         self.navigation_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
#         self.navigation_layout.addWidget(self.prev_button)
#         self.navigation_layout.addWidget(self.page_label)
#         self.navigation_layout.addWidget(self.next_button)
#         self.navigation_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

#         layout.addLayout(self.navigation_layout)
#         self.setLayout(layout)

#         # Maximize the window
#         self.setWindowState(Qt.WindowState.WindowMaximized)

#         # Connect buttons to methods
#         self.prev_button.clicked.connect(self.prev_page)
#         self.next_button.clicked.connect(self.next_page)

#         # Fetch and display the orders
#         self.fetch_orders()

#     def fetch_orders(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return
#             headers = {"Authorization": f"Bearer {token}"}
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos",
#                 headers=headers,
#             )
#             if res.status_code == 200:
#                 self.all_orders = res.json()
#                 self.update_table()  # Display the first 10 orders
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", f"{e}")
#             print(f"{e}")

#     def update_table(self):
#         # Calculate the start and end indices for the current page
#         start = (self.current_page - 1) * self.rows_per_page
#         end = start + self.rows_per_page
#         orders_to_show = self.all_orders[start:end]  # Get the data for the current page

#         # Populate the table with 10 rows
#         self.orders_table.setRowCount(len(orders_to_show))

#         for row_idx, order in enumerate(orders_to_show):
#             # Parse and format the createdAt field
#             created_at = order.get("createdAt", "")
#             if created_at:
#                 try:
#                     created_at = created_at.split(".")[0]  # Keeps only "2024-04-17T02:40:03"
#                     date_obj = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S")
#                     formatted_date = date_obj.strftime("%m/%d/%Y, %I:%M:%S %p")
#                 except ValueError:
#                     formatted_date = created_at  # Use original value if parsing fails
#             else:
#                 formatted_date = ""

#             # Add the order details to the table and center-align the text
#             self.add_centered_item(row_idx, 0, str(order.get("id", "")))
#             self.add_centered_item(row_idx, 1, formatted_date)
#             self.add_centered_item(row_idx, 2, order.get("customer_name", " "))
#             self.add_centered_item(row_idx, 3, order.get("customer_phone", ""))
#             self.add_centered_item(row_idx, 4, order.get("discountType", ""))
#             self.add_centered_item(row_idx, 5, str(order.get("discountAmount", "")))
#             self.add_centered_item(row_idx, 6, str(order.get("grandTotal", "")))

#         # Update the page number display
#         self.update_page_label()

#     def add_centered_item(self, row_idx, col_idx, text):
#         item = QTableWidgetItem(text)
#         item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center align the text
#         self.orders_table.setItem(row_idx, col_idx, item)

#     def update_page_label(self):
#         # Calculate the total number of pages
#         total_pages = (len(self.all_orders) + self.rows_per_page - 1) // self.rows_per_page
#         self.page_label.setText(f"Page {self.current_page} of {total_pages}")

#     def prev_page(self):
#         # Only allow navigating to previous page if it's not the first page
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.update_table()  # Update the table with previous 10 records

#     def next_page(self):
#         # Check if there are more records to load and move to the next page
#         total_pages = (len(self.all_orders) + self.rows_per_page - 1) // self.rows_per_page
#         if self.current_page < total_pages:
#             self.current_page += 1
#             self.update_table()  # Update the table with next 10 records


from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSpacerItem,
    QSizePolicy
)
from PyQt6.QtCore import Qt
from datetime import datetime
import requests
from utils.get_token import getToken

class OrderPage(QWidget):
    def __init__(self):
        super().__init__()

        # Pagination variables
        self.current_page = 1
        self.rows_per_page = 10
        self.all_orders = []  # Store all orders fetched from the API

        layout = QVBoxLayout()

        # Create table widget to display orders
        self.orders_table = QTableWidget()
        self.orders_table.setColumnCount(7)  # Adjust column count if necessary
        self.orders_table.setHorizontalHeaderLabels(
            [
                "ID",
                "Order Date",
                "Customer Name",
                "Customer Phone",
                "Discount Type",
                "Discount Value",
                "Total Price",
            ]
        )
        self.orders_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Styling table: center-align the headers, add borders, etc.
        self.orders_table.setStyleSheet("""
          
           
            QTableWidget::horizontalHeader {
                background-color: #0078d4;
                color: white;
                font-weight: bold;
                border: none;
            }
            QTableWidget::verticalHeader {
                background-color: #f1f1f1;
                color: #0078d4;
                font-weight: bold;
            }
            QHeaderView::section {
                background-color: #49A5AF;
                font-weight: bold;
                padding: 10px;
                border: 1px solid #ddd;
                color: black;
            }
           
        """)

        # Make columns stretch to fit the window
        self.orders_table.horizontalHeader().setStretchLastSection(True)
        self.orders_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Add the table to the layout
        layout.addWidget(self.orders_table)

        # Create navigation buttons (Previous, Next)
        self.navigation_layout = QHBoxLayout()

        # Styling smaller buttons
        self.prev_button = QPushButton("<")
        self.prev_button.setFixedSize(30, 30)
        self.page_label = QLabel("Page 1 of 1")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.next_button = QPushButton(">")
        self.next_button.setFixedSize(30, 30)

        # Add spacer items to center the buttons around the page number
        self.navigation_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.navigation_layout.addWidget(self.prev_button)
        self.navigation_layout.addWidget(self.page_label)
        self.navigation_layout.addWidget(self.next_button)
        self.navigation_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        layout.addLayout(self.navigation_layout)
        self.setLayout(layout)

        # Maximize the window
        self.setWindowState(Qt.WindowState.WindowMaximized)

        # Connect buttons to methods
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button.clicked.connect(self.next_page)

        # Fetch and display the orders
        self.fetch_orders()

    def fetch_orders(self):
        try:
            token = getToken()
            if not token:
                QMessageBox.warning(self, "Error", "Unauthenticated")
                return
            headers = {"Authorization": f"Bearer {token}"}
            res = requests.get(
                "https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos",
                headers=headers,
            )
            if res.status_code == 200:
                self.all_orders = res.json()
                self.update_table()  # Display the first 10 orders
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch data")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"{e}")
            print(f"{e}")

    def update_table(self):
        # Calculate the start and end indices for the current page
        start = (self.current_page - 1) * self.rows_per_page
        end = start + self.rows_per_page
        orders_to_show = self.all_orders[start:end]  # Get the data for the current page

        # Populate the table with 10 rows
        self.orders_table.setRowCount(len(orders_to_show))

        for row_idx, order in enumerate(orders_to_show):
            # Parse and format the createdAt field
            created_at = order.get("createdAt", "")
            if created_at:
                try:
                    created_at = created_at.split(".")[0]  # Keeps only "2024-04-17T02:40:03"
                    date_obj = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S")
                    formatted_date = date_obj.strftime("%m/%d/%Y, %I:%M:%S %p")
                except ValueError:
                    formatted_date = created_at  # Use original value if parsing fails
            else:
                formatted_date = ""

            # Add the order details to the table and center-align the text
            self.add_centered_item(row_idx, 0, str(order.get("id", "")))
            self.add_centered_item(row_idx, 1, formatted_date)
            self.add_centered_item(row_idx, 2, order.get("customer_name", " "))
            self.add_centered_item(row_idx, 3, order.get("customer_phone", ""))
            self.add_centered_item(row_idx, 4, order.get("discountType", ""))
            self.add_centered_item(row_idx, 5, str(order.get("discountAmount", "")))
            self.add_centered_item(row_idx, 6, str(order.get("grandTotal", "")))

        # Update the page number display
        self.update_page_label()

    def add_centered_item(self, row_idx, col_idx, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center align the text
        self.orders_table.setItem(row_idx, col_idx, item)

    def update_page_label(self):
        # Calculate the total number of pages
        total_pages = (len(self.all_orders) + self.rows_per_page - 1) // self.rows_per_page
        self.page_label.setText(f"Page {self.current_page} of {total_pages}")

    def prev_page(self):
        # Only allow navigating to previous page if it's not the first page
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()  # Update the table with previous 10 records

    def next_page(self):
        # Check if there are more records to load and move to the next page
        total_pages = (len(self.all_orders) + self.rows_per_page - 1) // self.rows_per_page
        if self.current_page < total_pages:
            self.current_page += 1
            self.update_table()  # Update the table with next 10 records
