from PyQt6.QtWidgets import QWidget,QVBoxLayout,QTableWidget,QMessageBox,QTableWidgetItem
from utils.get_token import getToken
import requests
class OrderPage(QWidget):
    def __init__(self):
        super().__init__()
        layout= QVBoxLayout()
        # create table widget to display orders
        self.orders_table = QTableWidget()
        self.orders_table.setColumnCount(6)
        self.orders_table.setHorizontalHeaderLabels(["ID","Order Date","Customer Name","Customer Phone","Discount Type","Discount Value","Total Price"])
        self.orders_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(self.orders_table)
        self.setLayout(layout)
        self.fetch_orders()
    
    def fetch_orders(self):
        try:
            token = getToken()
            # print(f'{token}')
            if not token:
                QMessageBox.warning(self,"Error","Unauthenticated")
                return 
            headers = {"Authorization":f"Bearer {token}"}
            res = requests.get("https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos", headers=headers)
            # print(res.json())
            if res.status_code==200:
                orders = res.json()
                self.populate_orders_table(orders)
            else:
                QMessageBox.warning(self,"Error","Failed to fetch data")
            
        except Exception as e:
            QMessageBox.warning(self,"Error",f'{e}')
            print(f'{e}')

    def populate_orders_table(self,orders):
        self.orders_table.setRowCount(len(orders))

        for row_idx,order in enumerate(orders):
            self.orders_table.setItem(row_idx,0,QTableWidgetItem(str(order.get("id",""))))
            self.orders_table.setItem(row_idx,1,QTableWidgetItem(str(order.get("createdAt",""))))
            self.orders_table.setItem(row_idx,2,QTableWidgetItem(order.get("customer_name"," ")))
            self.orders_table.setItem(row_idx,3,QTableWidgetItem(order.get("customer_phone","")))
            self.orders_table.setItem(row_idx,4,QTableWidgetItem(order.get("discountType","")))
            self.orders_table.setItem(row_idx,5,QTableWidgetItem(str(order.get("discountAmount",""))))
            self.orders_table.setItem(row_idx,6,QTableWidgetItem(str(order.get("grandTotal",""))))
    # def init_ui(self):
    #     layout = QVBoxLayout()
    #     title_lable = QLabel("Order no 1234")
    #     layout.addWidget(title_lable)
    #     self.setLayout(layout)