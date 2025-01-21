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


from PyQt6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,QSizePolicy,QHeaderView
from utils.get_token import getToken
import requests
from PyQt6.QtCore import Qt,QSize
class ProductPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout and window
        layout = QVBoxLayout()
        
        # create table for widgets
        self.product_table = QTableWidget()
        self.product_table.setColumnCount(3)
        self.product_table.setHorizontalHeaderLabels(["Id","Name","Vat"])
        self.product_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.product_table.setStyleSheet("""
    QTableWidget {
        border: 1px solid #ccc;
        font-size: 14px;
        border-radius: 5px;
    }
    QTableWidget::item {
        padding: 10px;
        border: 1px solid #ddd;
    }
    QHeaderView::section {
        background-color: #f2f2f2;
        font-weight: bold;
        padding: 10px;
        border: 1px solid #ddd;
        color: black;  # Set text color to black
    }
    QTableWidget::item:selected {
        background-color: #0078d4;
        color: white;
    }
""")
        
        # make the table expand to take available spaces
        self.product_table.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
         # Stretch the columns to equally take the available space
        self.product_table.horizontalHeader().setStretchLastSection(True)
        self.product_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.product_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.product_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.product_table)
        self.setLayout(layout)

        # Fetch and display the products
        self.fetch_products()

    def fetch_products(self):
        try:
            token = getToken()
            if not token:
                QMessageBox.warning(self, "Error", "Unauthenticated")
                return 
            
            headers = {"Authorization": f"Bearer {token}"}
            res = requests.get("https://anzaar-api.bitcommerz.com/api/v1/product/pos-products-for-shop", headers=headers)
            products = res.json()  # Assuming the response is in JSON format

            if not products:
                QMessageBox.warning(self, "No Data", "No products available.")
                return

            # Clear the table before adding new data
            self.table.setRowCount(0)

            # Populate the table with product data
            for product in products:
                row_position = self.table.rowCount()  # Get the current row count
                self.table.insertRow(row_position)  # Insert a new row

                # Assuming 'id', 'name', 'price', and 'stock' are the keys in the product data
                self.table.setItem(row_position, 0, QTableWidgetItem(str(product.get('id', 'N/A'))))
                self.table.setItem(row_position, 1, QTableWidgetItem(str(product.get('name', 'N/A'))))
                self.table.setItem(row_position, 2, QTableWidgetItem(str(product.get('price', 'N/A'))))
                self.table.setItem(row_position, 3, QTableWidgetItem(str(product.get('stock', 'N/A'))))

        except Exception as e:
            QMessageBox.warning(self, "Error", f'{e}')

