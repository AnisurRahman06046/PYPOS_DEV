# from PyQt6.QtWidgets import QWidget,QMessageBox, QVBoxLayout, QLabel
# from utils.get_token import getToken
# import requests
# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         layout = QVBoxLayout()
        
#         self.setWindowTitle("Product Page")
#         title = QLabel("Welcome to the Product Page!")
#         layout.addWidget(title)
#         self.setLayout(layout)
#         self.fetch_products()
        
#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self,"Error","Unauthenticated")
#                 return 
#             headers = {"Authorization":f"Bearer {token}"}
#             res = requests.get("https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop", headers=headers)
#             print(res.json())
#         except Exception as e:
#             QMessageBox.warning(self,"Error",f'{e}')


# from PyQt6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,QSizePolicy,QHeaderView
# from utils.get_token import getToken
# import requests
# from PyQt6.QtCore import Qt,QSize
# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set up the layout and window
#         layout = QVBoxLayout()
        
#         # create table for widgets
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["Id","Name","Vat"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
#         self.product_table.setStyleSheet("""
#     QTableWidget {
#         border: 1px solid #ccc;
#         font-size: 14px;
#         border-radius: 5px;
#     }
#     QTableWidget::item {
#         padding: 10px;
#         border: 1px solid #ddd;
#     }
#     QHeaderView::section {
#         background-color: #f2f2f2;
#         font-weight: bold;
#         padding: 10px;
#         border: 1px solid #ddd;
#         color: black;  # Set text color to black
#     }
#     QTableWidget::item:selected {
#         background-color: #0078d4;
#         color: white;
#     }
# """)
        
#         # make the table expand to take available spaces
#         self.product_table.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
#          # Stretch the columns to equally take the available space
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
#         self.product_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
#         self.product_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

#         layout.addWidget(self.product_table)
#         self.setLayout(layout)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return 
            
#             headers = {"Authorization": f"Bearer {token}"}
#             res = requests.get("https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop", headers=headers)
#             products = res.json()  # Assuming the response is in JSON format

#             if not products:
#                 QMessageBox.warning(self, "No Data", "No products available.")
#                 return

#             # Clear the table before adding new data
#             self.table.setRowCount(0)

#             # Populate the table with product data
#             for product in products:
#                 row_position = self.table.rowCount()  # Get the current row count
#                 self.table.insertRow(row_position)  # Insert a new row

#                 # Assuming 'id', 'name', 'price', and 'stock' are the keys in the product data
#                 self.table.setItem(row_position, 0, QTableWidgetItem(str(product.get('id', 'N/A'))))
#                 self.table.setItem(row_position, 1, QTableWidgetItem(str(product.get('name', 'N/A'))))
#                 self.table.setItem(row_position, 2, QTableWidgetItem(str(product.get('price', 'N/A'))))
#                 self.table.setItem(row_position, 3, QTableWidgetItem(str(product.get('stock', 'N/A'))))

#         except Exception as e:
#             QMessageBox.warning(self, "Error", f'{e}')



# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
# )
# from PyQt6.QtCore import Qt
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         self.product_table.setStyleSheet("""
#             QTableWidget {
#                 border: 1px solid #ccc;
#                 font-size: 14px;
#                 border-radius: 5px;
#             }
#             QTableWidget::item {
#                 padding: 10px;
#                 border: 1px solid #ddd;
#             }
#             QHeaderView::section {
#                 background-color: #f2f2f2;
#                 font-weight: bold;
#                 padding: 10px;
#                 border: 1px solid #ddd;
#                 color: black;
#             }
#             QTableWidget::item:selected {
#                 background-color: #0078d4;
#                 color: white;
#             }
#         """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

#         layout.addWidget(self.product_table)
#         self.setLayout(layout)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )
#             if res.status_code == 200:
#                 products = res.json()
#                 self.populate_product_table(products)
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def populate_product_table(self, products):
#         self.product_table.setRowCount(len(products))

#         for row_idx, product in enumerate(products):
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(str(product.get("id", "N/A"))))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(product.get("name", "N/A")))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(str(product.get("vat", "N/A"))))

# ---------------------------------**************------------


# updated code
# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
# )
# from PyQt6.QtCore import Qt
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         self.product_table.setStyleSheet("""
#             QTableWidget {
#                 border: 1px solid #ccc;
#                 font-size: 14px;
#                 border-radius: 5px;
#             }
#             QTableWidget::item {
#                 padding: 10px;
#                 border: 1px solid #ddd;
#             }
#             QHeaderView::section {
#                 background-color: #f2f2f2;
#                 font-weight: bold;
#                 padding: 10px;
#                 border: 1px solid #ddd;
#                 color: black;
#             }
#             QTableWidget::item:selected {
#                 background-color: #0078d4;
#                 color: white;
#             }
#         """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

#         layout.addWidget(self.product_table)
#         self.setLayout(layout)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )
#             if res.status_code == 200:
#                 products = res.json()["data"]
#                 self.populate_product_table(products)
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def populate_product_table(self, products):
#         self.product_table.setRowCount(len(products))

#         for row_idx, product in enumerate(products):
#             # Get the data for each column
#             product_id = str(product.get("id", "N/A"))
#             name = product.get("name", "N/A")
#             vat = str(product.get("vat", "0"))

#             # Populate the table
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(product_id))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(name))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(vat))




# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
#     QHBoxLayout,
#     QPushButton
# )
# from PyQt6.QtCore import Qt
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Pagination variables
#         self.current_page = 1
#         self.rows_per_page = 10
#         self.all_products = []  # Store all products fetched from the API

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         self.product_table.setStyleSheet("""
#             QTableWidget {
               
#                 font-size: 14px;
#             }
#             QTableWidget::item {
#                 padding: 10px;
#                 border: 1px solid #ddd;
#             }
#             QHeaderView::section {
#                 background-color: #f2f2f2;
#                 font-weight: bold;
#                 padding: 10px;
#                 border: 1px solid #ddd;
#                 color: black;
#             }
#             QTableWidget::item:selected {
#                 background-color: #0078d4;
#                 color: white;
#             }
#         """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

#         # Create navigation buttons (Previous, Next)
#         self.navigation_layout = QHBoxLayout()
#         self.prev_button = QPushButton("Previous")
#         self.next_button = QPushButton("Next")
#         self.navigation_layout.addWidget(self.prev_button)
#         self.navigation_layout.addWidget(self.next_button)

#         layout.addWidget(self.product_table)
#         layout.addLayout(self.navigation_layout)
#         self.setLayout(layout)

#         # Connect buttons to methods
#         self.prev_button.clicked.connect(self.prev_page)
#         self.next_button.clicked.connect(self.next_page)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
            
#             # Make the API request to fetch all product data
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )

#             if res.status_code == 200:
#                 self.all_products = res.json()["data"]
#                 self.update_table()  # Display the first 10 products
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def update_table(self):
#         # Calculate the start and end indices for the current page
#         start = (self.current_page - 1) * self.rows_per_page
#         end = start + self.rows_per_page
#         products_to_show = self.all_products[start:end]  # Get the data for the current page

#         # Populate the table with 10 rows
#         self.product_table.setRowCount(len(products_to_show))

#         for row_idx, product in enumerate(products_to_show):
#             # Get the data for each column
#             product_id = str(product.get("id", "N/A"))
#             name = product.get("name", "N/A")
#             vat = str(product.get("vat", "0"))

#             # Populate the table
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(product_id))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(name))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(vat))

#     def prev_page(self):
#         # Only allow navigating to previous page if it's not the first page
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.update_table()  # Update the table with previous 10 records

#     def next_page(self):
#         # Check if there are more records to load and move to the next page
#         if self.current_page * self.rows_per_page < len(self.all_products):
#             self.current_page += 1
#             self.update_table()  # Update the table with next 10 records



# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
#     QHBoxLayout,
#     QPushButton,
#     QLabel
# )
# from PyQt6.QtCore import Qt
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Pagination variables
#         self.current_page = 1
#         self.rows_per_page = 10
#         self.all_products = []  # Store all products fetched from the API

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         self.product_table.setStyleSheet("""
#             QTableWidget {
#                 border: 1px solid #ccc;
#                 font-size: 14px;
#                 border-radius: 5px;
#             }
#             QTableWidget::item {
#                 padding: 10px;
#                 border: 1px solid #ddd;
#             }
#             QHeaderView::section {
#                 background-color: #f2f2f2;
#                 font-weight: bold;
#                 padding: 10px;
#                 border: 1px solid #ddd;
#                 color: black;
#             }
#             QTableWidget::item:selected {
#                 background-color: #0078d4;
#                 color: white;
#             }
#         """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

#         # Create navigation buttons (Previous, Next)
#         self.navigation_layout = QHBoxLayout()
#         self.prev_button = QPushButton("Previous")
#         self.page_label = QLabel("Page 1 of 1")
#         self.next_button = QPushButton("Next")
#         self.navigation_layout.addWidget(self.prev_button)
#         self.navigation_layout.addWidget(self.page_label)
#         self.navigation_layout.addWidget(self.next_button)

#         layout.addWidget(self.product_table)
#         layout.addLayout(self.navigation_layout)
#         self.setLayout(layout)

#         # Connect buttons to methods
#         self.prev_button.clicked.connect(self.prev_page)
#         self.next_button.clicked.connect(self.next_page)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
            
#             # Make the API request to fetch all product data
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )

#             if res.status_code == 200:
#                 self.all_products = res.json()["data"]
#                 self.update_table()  # Display the first 10 products
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def update_table(self):
#         # Calculate the start and end indices for the current page
#         start = (self.current_page - 1) * self.rows_per_page
#         end = start + self.rows_per_page
#         products_to_show = self.all_products[start:end]  # Get the data for the current page

#         # Populate the table with 10 rows
#         self.product_table.setRowCount(len(products_to_show))

#         for row_idx, product in enumerate(products_to_show):
#             # Get the data for each column
#             product_id = str(product.get("id", "N/A"))
#             name = product.get("name", "N/A")
#             vat = str(product.get("vat", "0"))

#             # Populate the table
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(product_id))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(name))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(vat))

#         # Update the page number display
#         self.update_page_label()

#     def update_page_label(self):
#         # Calculate the total number of pages
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
#         self.page_label.setText(f"Page {self.current_page} of {total_pages}")

#     def prev_page(self):
#         # Only allow navigating to previous page if it's not the first page
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.update_table()  # Update the table with previous 10 records

#     def next_page(self):
#         # Check if there are more records to load and move to the next page
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
#         if self.current_page < total_pages:
#             self.current_page += 1
#             self.update_table()  # Update the table with next 10 records



# from PyQt6.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QMessageBox,
#     QTableWidgetItem,
#     QHeaderView,
#     QHBoxLayout,
#     QPushButton,
#     QLabel
# )
# from PyQt6.QtCore import Qt
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Pagination variables
#         self.current_page = 1
#         self.rows_per_page = 10
#         self.all_products = []  # Store all products fetched from the API

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         self.product_table.setStyleSheet("""
#             QTableWidget {
#                 border: 1px solid #ccc;
#                 font-size: 14px;
#                 border-radius: 5px;
#             }
#             QTableWidget::item {
#                 padding: 10px;
#                 border: 1px solid #ddd;
#             }
#             QHeaderView::section {
#                 background-color: #f2f2f2;
#                 font-weight: bold;
#                 padding: 10px;
#                 border: 1px solid #ddd;
#                 color: black;
#             }
#             QTableWidget::item:selected {
#                 background-color: #0078d4;
#                 color: white;
#             }
#         """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

#         # Create navigation buttons (Previous, Next)
#         self.navigation_layout = QHBoxLayout()
        
#         # Styling smaller buttons
#         self.prev_button = QPushButton("<")
#         self.prev_button.setFixedSize(30, 30)
#         self.page_label = QLabel("Page 1 of 1")
#         self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.next_button = QPushButton(">")
#         self.next_button.setFixedSize(30, 30)

#         self.navigation_layout.addWidget(self.prev_button)
#         self.navigation_layout.addWidget(self.page_label)
#         self.navigation_layout.addWidget(self.next_button)

#         layout.addWidget(self.product_table)
#         layout.addLayout(self.navigation_layout)
#         self.setLayout(layout)

#         # Connect buttons to methods
#         self.prev_button.clicked.connect(self.prev_page)
#         self.next_button.clicked.connect(self.next_page)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
            
#             # Make the API request to fetch all product data
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )

#             if res.status_code == 200:
#                 self.all_products = res.json()["data"]
#                 self.update_table()  # Display the first 10 products
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def update_table(self):
#         # Calculate the start and end indices for the current page
#         start = (self.current_page - 1) * self.rows_per_page
#         end = start + self.rows_per_page
#         products_to_show = self.all_products[start:end]  # Get the data for the current page

#         # Populate the table with 10 rows
#         self.product_table.setRowCount(len(products_to_show))

#         for row_idx, product in enumerate(products_to_show):
#             # Get the data for each column
#             product_id = str(product.get("id", "N/A"))
#             name = product.get("name", "N/A")
#             vat = str(product.get("vat", "0"))

#             # Populate the table
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(product_id))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(name))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(vat))

#         # Update the page number display
#         self.update_page_label()

#     def update_page_label(self):
#         # Calculate the total number of pages
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
#         self.page_label.setText(f"Page {self.current_page} of {total_pages}")

#     def prev_page(self):
#         # Only allow navigating to previous page if it's not the first page
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.update_table()  # Update the table with previous 10 records

#     def next_page(self):
#         # Check if there are more records to load and move to the next page
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
#         if self.current_page < total_pages:
#             self.current_page += 1
#             self.update_table()  # Update the table with next 10 records


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
# from utils.get_token import getToken
# import requests


# class ProductPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Pagination variables
#         self.current_page = 1
#         self.rows_per_page = 10
#         self.all_products = []  # Store all products fetched from the API

#         # Set up the layout and window
#         layout = QVBoxLayout()

#         # Create table widget for products
#         self.product_table = QTableWidget()
#         self.product_table.setColumnCount(3)
#         self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
#         self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

#         # Style the table
#         # self.product_table.setStyleSheet("""
#         #     QTableWidget {
#         #         border: 1px solid #ccc;
#         #         font-size: 14px;
#         #         border-radius: 5px;
#         #     }
#         #     QTableWidget::item {
#         #         padding: 10px;
#         #         border: 1px solid #ddd;
#         #     }
#         #     QHeaderView::section {
#         #         background-color: #f2f2f2;
#         #         font-weight: bold;
#         #         padding: 10px;
#         #         border: 1px solid #ddd;
#         #         color: black;
#         #     }
#         #     QTableWidget::item:selected {
#         #         background-color: #0078d4;
#         #         color: white;
#         #     }
#         # """)

#         # Make columns stretch to fit the window
#         self.product_table.horizontalHeader().setStretchLastSection(True)
#         self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

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

#         layout.addWidget(self.product_table)
#         layout.addLayout(self.navigation_layout)
#         self.setLayout(layout)

#         # Connect buttons to methods
#         self.prev_button.clicked.connect(self.prev_page)
#         self.next_button.clicked.connect(self.next_page)

#         # Fetch and display the products
#         self.fetch_products()

#     def fetch_products(self):
#         try:
#             token = getToken()
#             if not token:
#                 QMessageBox.warning(self, "Error", "Unauthenticated")
#                 return

#             headers = {"Authorization": f"Bearer {token}"}
            
#             # Make the API request to fetch all product data
#             res = requests.get(
#                 "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
#                 headers=headers,
#             )

#             if res.status_code == 200:
#                 self.all_products = res.json()["data"]
#                 self.update_table()  # Display the first 10 products
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch product data")
#         except Exception as e:
#             QMessageBox.warning(self, "Error", str(e))

#     def update_table(self):
#         # Calculate the start and end indices for the current page
#         start = (self.current_page - 1) * self.rows_per_page
#         end = start + self.rows_per_page
#         products_to_show = self.all_products[start:end]  # Get the data for the current page

#         # Populate the table with 10 rows
#         self.product_table.setRowCount(len(products_to_show))

#         for row_idx, product in enumerate(products_to_show):
#             # Get the data for each column
#             product_id = str(product.get("id", "N/A"))
#             name = product.get("name", "N/A")
#             vat = str(product.get("vat", "0"))

#             # Populate the table
#             self.product_table.setItem(row_idx, 0, QTableWidgetItem(product_id))
#             self.product_table.setItem(row_idx, 1, QTableWidgetItem(name))
#             self.product_table.setItem(row_idx, 2, QTableWidgetItem(vat))

#         # Update the page number display
#         self.update_page_label()

#     def update_page_label(self):
#         # Calculate the total number of pages
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
#         self.page_label.setText(f"Page {self.current_page} of {total_pages}")

#     def prev_page(self):
#         # Only allow navigating to previous page if it's not the first page
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.update_table()  # Update the table with previous 10 records

#     def next_page(self):
#         # Check if there are more records to load and move to the next page
#         total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
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
from utils.get_token import getToken
import requests


class ProductPage(QWidget):
    def __init__(self):
        super().__init__()

        # Pagination variables
        self.current_page = 1
        self.rows_per_page = 10
        self.all_products = []  # Store all products fetched from the API

        # Set up the layout and window
        layout = QVBoxLayout()

        # Create table widget for products
        self.product_table = QTableWidget()
        self.product_table.setColumnCount(3)
        self.product_table.setHorizontalHeaderLabels(["ID", "Name", "VAT"])
        self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Style the table
        self.product_table.setStyleSheet("""
            
            
            QHeaderView::section {
                background-color: #49A5AF;
                font-weight: bold;
                padding: 10px;
                border: 1px solid #ddd;
                color: black;
            }
            QTableWidget::horizontalHeader {
                background-color: #49A5AF;
                font-weight: bold;
                padding: 10px;
                border: 1px solid #ddd;
                color: black;
            }
           
        """)

        # Make columns stretch to fit the window
        self.product_table.horizontalHeader().setStretchLastSection(True)
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

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

        layout.addWidget(self.product_table)
        layout.addLayout(self.navigation_layout)
        self.setLayout(layout)

        # Connect buttons to methods
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button.clicked.connect(self.next_page)

        # Fetch and display the products
        self.fetch_products()

    def fetch_products(self):
        try:
            token = getToken()
            if not token:
                QMessageBox.warning(self, "Error", "Unauthenticated")
                return

            headers = {"Authorization": f"Bearer {token}"}
            
            # Make the API request to fetch all product data
            res = requests.get(
                "https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop",
                headers=headers,
            )

            if res.status_code == 200:
                self.all_products = res.json()["data"]
                self.update_table()  # Display the first 10 products
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch product data")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def update_table(self):
        # Calculate the start and end indices for the current page
        start = (self.current_page - 1) * self.rows_per_page
        end = start + self.rows_per_page
        products_to_show = self.all_products[start:end]  # Get the data for the current page

        # Populate the table with 10 rows
        self.product_table.setRowCount(len(products_to_show))

        for row_idx, product in enumerate(products_to_show):
            # Get the data for each column
            product_id = str(product.get("id", "N/A"))
            name = product.get("name", "N/A")
            vat = str(product.get("vat", "0"))

            # Populate the table and center align the text
            product_id_item = QTableWidgetItem(product_id)
            name_item = QTableWidgetItem(name)
            vat_item = QTableWidgetItem(vat)

            # Set text alignment to center
            product_id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            vat_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Insert the items in the table
            self.product_table.setItem(row_idx, 0, product_id_item)
            self.product_table.setItem(row_idx, 1, name_item)
            self.product_table.setItem(row_idx, 2, vat_item)

        # Update the page number display
        self.update_page_label()

    def update_page_label(self):
        # Calculate the total number of pages
        total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
        self.page_label.setText(f"Page {self.current_page} of {total_pages}")

    def prev_page(self):
        # Only allow navigating to previous page if it's not the first page
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()  # Update the table with previous 10 records

    def next_page(self):
        # Check if there are more records to load and move to the next page
        total_pages = (len(self.all_products) + self.rows_per_page - 1) // self.rows_per_page
        if self.current_page < total_pages:
            self.current_page += 1
            self.update_table()  # Update the table with next 10 records
