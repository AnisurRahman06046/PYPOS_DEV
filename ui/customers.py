from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel

class CustomerPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        title = QLabel("Welcome to Customer Page")
        
        layout.addWidget(title)
        self.setLayout(layout)