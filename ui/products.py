from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
class ProductPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        self.setWindowTitle("Product Page")
        title = QLabel("Welcome to the Product Page!")
        layout.addWidget(title)
        self.setLayout(layout)
